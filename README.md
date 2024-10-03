# BAC Calculator

## Overview

The BAC Calculator is a command-line tool that estimates Blood Alcohol Content (BAC) based on user input. It helps users understand their current BAC levels, how many drinks they need to reach the "Ballmer Peak," and provides a history of past calculations.

## What is the Ballmer Peak?

The Ballmer Peak is an informal and humorous concept in the programming community, named after Steve Ballmer, former CEO of Microsoft. It suggests that there is an optimal range of Blood Alcohol Content (approximately 0.129) that enhances cognitive performance and creativity, particularly for software developers. The idea is that a moderate level of intoxication can lead to increased productivity, while too little or too much alcohol can hinder performance.

## How the Calculator Works

### BAC Calculation

The calculator estimates BAC using the following formula:

**BAC** = ((A × 5.14) / (weight × r)) - (0.015 × hours)


- **A**: Total ounces of alcohol consumed (number of drinks multiplied by ounces per drink).
- **weight**: User's weight in pounds.
- **r**: Widmark factor (0.68 for males, 0.55 for females).
- **hours**: Time since the first drink, which decreases BAC over time at a rate of 0.015 per hour.

### Reaching the Ballmer Peak

To determine how many additional drinks are needed to reach the Ballmer Peak, the calculator uses the following logic:

1. **Current BAC Check**: If the current BAC is already at or above the target (0.129), no additional drinks are needed.
2. **Calculate Required BAC**: The calculator computes how much more BAC is needed to reach 0.129.
3. **Calculate Additional Drinks**: It uses the formula derived from the BAC calculation to estimate how many additional drinks would be necessary to achieve the target BAC.

### Time to Reach Ballmer Peak

If the current BAC exceeds the target of 0.129, the calculator estimates how long it will take to drop back to the Ballmer Peak. This is calculated using the formula:

**Time to drop** = (current BAC - 0.129) / 0.015


## Features

- **Calculate Current BAC**: Input the number of drinks, weight, gender, and time since the first drink to get an estimated BAC.
- **View BAC History**: Display a history of BAC calculations stored in a JSON file.
- **Delete BAC History**: Clear all stored BAC calculations.
- **Statistics**: View average, highest, and lowest BAC from history.

## Requirements

- Python 3.x
- `rich` library for enhanced console output.

You can install the required library using pip:

```bash
pip install rich
```

## How to Use

1. **Run the Program**: Execute the script in a terminal.
   
   ```bash
   python bac_calculator.py
   ```

2. **Choose an Option**: The main menu will display options:
   - **1**: Calculate BAC
   - **2**: View BAC History
   - **3**: Delete BAC History
   - **4**: Exit

3. **Input Data**: If calculating BAC, input the required details:
   - Number of drinks consumed
   - Ounces per drink (default is 1.5)
   - Weight in pounds
   - Gender (male/female)
   - Time since first drink in hours

4. **View Results**: The program will display the calculated BAC, additional drinks needed to reach the Ballmer Peak, and the time until BAC drops to the optimal level, if applicable.

5. **Save History**: The BAC calculation will be automatically saved in a JSON file for future reference.

## Data Persistence

- **BAC History**: The program stores the history of BAC calculations in a JSON file named `bac_history.json`. This file is created in the same directory as the script.

## JSON Structure

The JSON file will contain an array of entries, where each entry is a tuple of the timestamp and the BAC value:

```json
[
    ["2024-10-01 12:00:00", 0.0854],
    ["2024-10-02 14:30:00", 0.1200]
]
```

## Notes

- The Ballmer Peak is considered an informal and humorous concept; please drink responsibly.
- The BAC estimates may not be accurate for all individuals due to varying factors such as metabolism, health conditions, and alcohol tolerance.

## License

This project is open-source. Feel free to modify and distribute it, but please attribute the original creator.

## Contact

For any questions or feedback, feel free to reach out!

Kind Regards, 
Jaq Shanahan