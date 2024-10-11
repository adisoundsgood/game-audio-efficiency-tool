# Game Audio Efficiency Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A python-based tool for analyzing and optimizing audio event usage in game development.

## Table of Contents

- [Purpose](#purpose)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Understanding the Report](#understanding-the-report)
- [Value of the Report](#value-of-the-report)
- [Extending the Tool](#extending-the-tool)
- [Contributing](#contributing)
- [License](#license)

## Purpose

The Audio Scripting Efficiency Tool is designed to analyze the use of audio events in game development. It provides insights into how audio events are utilized across different levels of your game, helping to identify potential issues and opportunities for optimization.

## Features

- 🔍 Identifies unused audio events
- 🔊 Highlights overused audio events
- 📊 Provides a distribution of audio event usage
- 💾 Estimates potential memory savings from unused events
- 🎮 Allows for analysis of all levels or specific levels

## Installation

### Prerequisites

- Python 3.6 or newer
- Access to your game's Wwise project XML export
- JSON files representing audio event usage in each level

### Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/audio-scripting-efficiency-tool.git
   cd audio-scripting-efficiency-tool
   ```

2. Ensure your file structure is set up as follows:
   ```
   audio-scripting-efficiency-tool/
   ├── src/
   │   └── tool.py
   └── examples/
       ├── wise_events.xml
       └── game_scripts/
           ├── level1.json
           ├── level2.json
           └── level3.json
   ```

3. The `wise_events.xml` file should be an export from your Wwise project containing all event definitions.
4. Each `levelX.json` file should contain an array of audio events used in that level, like this:
   ```json
   {
     "audio_events": ["Play_Footstep", "Play_Explosion", "Play_Music"]
   }
   ```

## Usage

1. Open a terminal or command prompt.
2. Navigate to the `src` directory.
3. Run the tool using one of the following commands:

   - To analyze all levels:
     ```
     python tool.py
     ```

   - To analyze a specific level (e.g., level1):
     ```
     python tool.py --level level1
     ```

## Understanding the Report

The tool generates a report with the following sections:

### 1. Unused Wwise Events

Lists any events defined in Wwise but not used in the analyzed level(s). This helps identify potential memory savings and keeps your project clean.

### 2. Overused Events

Highlights events used more than 100 times. This can help identify areas where more audio variety might be beneficial.

### 3. Event Usage Distribution

Provides a breakdown of how frequently events are used, categorized into bins (0-1, 1-10, 10-50, 50-100, 100+ uses).

## Value of the Report

### For Audio Directors

- Optimize memory usage by identifying and removing unused events
- Ensure efficient use of audio resources across the project
- Make informed decisions about where to allocate time and resources for audio improvements

### For Sound Designers

- Identify areas where more audio variety could enhance the player experience
- Understand how your audio events are being utilized across different levels
- Spot potential issues, such as overused events or underutilized sound designs

## Extending the Tool

The Audio Scripting Efficiency Tool is designed to be extensible. Here are some ways you could enhance its functionality:

1. **Custom Thresholds**: Modify the `find_overused_events` method to accept a custom threshold for what's considered "overused".

2. **Additional Metrics**: Add new methods to calculate other useful metrics, such as:
   - Average number of unique events per level
   - Most commonly used events across all levels
   - Correlation between level length and number of audio events

3. **Integration with Wwise**: Enhance the tool to read directly from Wwise project files rather than XML exports.

4. **Graphical Output**: Implement visualization of the data using libraries like matplotlib or plotly.

5. **Real-time Monitoring**: Adapt the tool to work with your game's logging system for real-time audio event usage tracking during playtesting.

6. **Audio Category Analysis**: If your events follow a naming convention that includes categories (e.g., SFX, Music, VO), add functionality to analyze usage patterns by category.

To implement these extensions, you'll need to modify the `EnhancedAudioScriptingTool` class in `tool.py`. If you're not comfortable with Python programming, consider collaborating with a technical audio designer or programmer to implement these enhancements.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For any questions, suggestions, or assistance with extending the tool, please open an issue or reach out to Adi @ adityasuiyer@gmail.com
