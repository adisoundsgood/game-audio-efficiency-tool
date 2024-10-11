import json
import os
import xml.etree.ElementTree as ET
from collections import Counter
import argparse

class AudioScriptingTool:
    def __init__(self):
        self.wwise_events = {}
        self.game_scripts = {}
        self.event_usage_count = Counter()
        self.event_memory_usage = {}

    def load_wwise_events(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        for event in root.findall(".//Event"):
            event_id = event.get('ID')
            self.wwise_events[event.get('Name')] = {
                'id': event_id,
                'memory': self.calculate_event_memory(event_id, root)
            }

    def calculate_event_memory(self, event_id, root):
        # This is a simplified estimation. In a real scenario, you'd need more complex logic
        # to accurately calculate memory usage based on audio file sizes, compression, etc.
        memory = 0
        for action in root.findall(f".//Event[@ID='{event_id}']//*[@ObjectPath]"):
            object_path = action.get('ObjectPath')
            if 'SFX' in object_path:  # Assume SFX are loaded in memory
                memory += 1024 * 1024  # Arbitrary 1MB per SFX for this example
        return memory

    def load_game_scripts(self, directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.json'):
                    with open(os.path.join(root, file), 'r') as f:
                        script_data = json.load(f)
                        self.game_scripts[file] = script_data
                        self.count_event_usage(script_data)

    def count_event_usage(self, script_data):
        if 'audio_events' in script_data:
            self.event_usage_count.update(script_data['audio_events'])

    def find_unused_events(self):
        return set(self.wwise_events.keys()) - set(self.event_usage_count.keys())

    def calculate_potential_memory_savings(self, unused_events):
        return sum(self.wwise_events[event]['memory'] for event in unused_events)

    def find_overused_events(self, threshold=100):
        return {event: count for event, count in self.event_usage_count.items() if count > threshold}

    def generate_report(self):
        unused_events = self.find_unused_events()
        overused_events = self.find_overused_events()
        potential_memory_savings = self.calculate_potential_memory_savings(unused_events)

        report = f"Audio Performance Analysis Report\n"
        report += f"================================\n\n"
        report += f"1. Unused Wwise Events ({len(unused_events)}):\n"
        for event in sorted(unused_events):
            report += f"   - {event} (ID: {self.wwise_events[event]['id']}, Est. Memory: {self.wwise_events[event]['memory'] / 1024:.2f} KB)\n"
        report += f"\nPotential memory savings: {potential_memory_savings / (1024 * 1024):.2f} MB\n\n"
        
        report += f"2. Overused Events (>100 uses):\n"
        for event, count in sorted(overused_events.items(), key=lambda x: x[1], reverse=True):
            report += f"   - {event}: {count} uses\n"
        
        report += f"\n3. Event Usage Distribution:\n"
        usage_bins = [0, 1, 10, 50, 100, float('inf')]
        usage_counts = [sum(1 for count in self.event_usage_count.values() if low <= count < high) 
                        for low, high in zip(usage_bins, usage_bins[1:])]
        for bin_start, bin_end, count in zip(usage_bins, usage_bins[1:], usage_counts):
            report += f"   {bin_start}-{bin_end if bin_end != float('inf') else '+'} uses: {count} events\n"

        return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze audio events in game scripts.")
    parser.add_argument("--level", help="Specify a level name to analyze (e.g., 'level1')")
    args = parser.parse_args()

    # Get the current script's directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct paths relative to the script's location
    wwise_events_path = os.path.join(current_dir, '..', 'examples', 'wise_events.xml')
    game_scripts_path = os.path.join(current_dir, '..', 'examples', 'game_scripts')

    tool = AudioScriptingTool()
    tool.load_wwise_events(wwise_events_path)
    tool.load_game_scripts(game_scripts_path)
    print(tool.generate_report())