import json

## global run list
run = []

def load_data(filename="run_data.json"):
    # Load existing runs if the file exists
    pass

def save_data(filename="run_data.json"):
    # Save run list to JSON
    pass

def add_run():
    # prompt user for date, pace, distance, time, notes
    # calculate pace = time / distance
    # Append run to run list
    pass

def view_runs():
    # Loop through all runs in list and print each one
    pass

def total_mileage():
    # sum distance miles for all runs
    pass

def average_pace():
    # calculate the overall average pace
    pass

def main():
    load_data()
    while True:
        print("\n====Runner Tracker===")
        print("1. Add new run")
        print("2. View all runs")
        print("3. View total mileage")
        print("4. View average pace")
        print("5. Save and exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_run()
        elif choice == "2":
            view_runs()
        elif choice == "3":
            total_mileage()
        elif choice == "4":
            average_pace()
        elif choice == "5":
            save_data()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")