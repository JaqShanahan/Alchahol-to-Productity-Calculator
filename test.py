import random
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def calculate_bac(drinks, ounces_per_drink, weight, gender, hours):
    r = 0.68 if gender.lower() == 'male' else 0.55
    A = drinks * ounces_per_drink
    bac = (A * 5.14 / (weight * r)) - (0.015 * hours)
    return bac

def drinks_needed_to_reach_ballmer(current_bac, weight, gender, target_bac=0.129, ounces_per_drink=1.5):
    if current_bac >= target_bac:
        return 0
    required_bac = target_bac - current_bac
    additional_drinks = required_bac * (weight * (0.68 if gender.lower() == 'male' else 0.55)) / (5.14 / ounces_per_drink)
    return max(0, round(additional_drinks))

def time_to_ballmer_peak(current_bac, target_bac=0.129, rate=0.015):
    if current_bac > target_bac:
        return (current_bac - target_bac) / rate
    return 0

def bac_status(current_bac, target_bac=0.129):
    if current_bac < target_bac:
        return "Below Ballmer Peak"
    elif current_bac == target_bac:
        return "At Ballmer Peak"
    else:
        return "Above Ballmer Peak"

def display_bac_history(history):
    if not history:
        console.print("No BAC history available.", style="yellow")
        return
    table = Table(title="BAC History")
    table.add_column("Date & Time", style="cyan")
    table.add_column("BAC", style="magenta")
    for entry in history:
        timestamp, bac = entry
        table.add_row(timestamp.strftime("%Y-%m-%d %H:%M:%S"), f"{bac:.4f}")
    console.print(table)

def save_bac_history_to_json(history, filename="bac_history.json"):
    with open(filename, 'w') as f:
        json_data = [(timestamp.strftime("%Y-%m-%d %H:%M:%S"), bac) for timestamp, bac in history]
        json.dump(json_data, f, indent=4)

def load_bac_history_from_json(filename="bac_history.json"):
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            if not content:
                console.print("The history file is empty. Starting fresh.", style="yellow")
                return []
            data = json.loads(content)
            return [(datetime.strptime(entry[0], "%Y-%m-%d %H:%M:%S"), entry[1]) for entry in data]
    except FileNotFoundError:
        console.print("No history file found. Starting fresh.", style="yellow")
        return []
    except json.JSONDecodeError:
        console.print("Error decoding JSON. Starting fresh.", style="red")
        return []

def delete_bac_history():
    return []

def calculate_summary_statistics(history):
    if not history:
        return None
    bac_values = [bac for _, bac in history]
    return {
        "average": sum(bac_values) / len(bac_values),
        "highest": max(bac_values),
        "lowest": min(bac_values)
    }

def main():
    bac_history = load_bac_history_from_json()

    while True:
        console.print("Welcome to the BAC Calculator!", style="bold green")
        console.print("\n1. Calculate BAC")
        console.print("2. View BAC History")
        console.print("3. Delete BAC History")
        console.print("4. Exit")
        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4"])

        if choice == "1":
            drinks = int(Prompt.ask("Enter the number of drinks consumed", default="1"))
            ounces_per_drink = float(Prompt.ask("Enter the ounces per drink (default is 1.5)", default="1.5"))
            weight = int(Prompt.ask("Enter your weight in pounds", default="180"))
            gender = Prompt.ask("Enter your gender (male/female)", choices=["male", "female"])
            hours = float(Prompt.ask("Enter the time since first drink in hours", default="0"))

            # Calculate current BAC
            current_bac = calculate_bac(drinks, ounces_per_drink, weight, gender, hours)
            bac_history.append((datetime.now(), current_bac))

            # Create a table for output
            table = Table(title="BAC Calculator Results")
            table.add_column("Metric", style="cyan")
            table.add_column("Value", style="magenta")

            # Adding calculated values to the table
            table.add_row("Estimated BAC", f"{current_bac:.4f}")
            additional_drinks = drinks_needed_to_reach_ballmer(current_bac, weight, gender)
            table.add_row("Additional drinks needed", str(additional_drinks))

            # Calculate time to drop to Ballmer Peak if over
            time_needed = time_to_ballmer_peak(current_bac)

            if current_bac > 0.129:
                margin_of_error = random.uniform(0.1, 0.5)
                time_lower = max(0, time_needed - margin_of_error)
                time_upper = time_needed + margin_of_error
                table.add_row("Time until dropping to Ballmer Peak", f"{time_lower:.2f} to {time_upper:.2f} hours")

            # Check BAC status and add to the table
            status = bac_status(current_bac)
            table.add_row("Current BAC status", status)

            # Print the results table
            console.print(table)

            # Save the BAC history to a JSON file
            save_bac_history_to_json(bac_history)

        elif choice == "2":
            display_bac_history(bac_history)
            stats = calculate_summary_statistics(bac_history)
            if stats:
                console.print("\nSummary Statistics:")
                console.print(f"Average BAC: {stats['average']:.4f}")
                console.print(f"Highest BAC: {stats['highest']:.4f}")
                console.print(f"Lowest BAC: {stats['lowest']:.4f}")

        elif choice == "3":
            bac_history = delete_bac_history()
            console.print("BAC history deleted.", style="bold red")

        elif choice == "4":
            console.print("Exiting the program. Goodbye!", style="bold red")
            break

if __name__ == "__main__":
    main()
