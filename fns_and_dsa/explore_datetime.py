from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days_to_add):
    """
    Calculate a future date based on the current date and the number of days to add.

    Args:
        days_to_add (int): The number of days to add to the current date.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    display_current_datetime()
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days_to_add)

if __name__ == "__main__":
    main()
