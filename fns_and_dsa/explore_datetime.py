# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add: "))
        future_date = datetime.now() + timedelta(days=days_to_add)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print(f"Future Date: {formatted_future}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()