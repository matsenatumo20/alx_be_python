task = input("Enter a task description: ")
priority = input("Enter the task's priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

# Process the Task Based on Priority and Time Sensitivity
match priority.lower():
    case "high":
        reminder = f"High priority task: {task}"
    case "medium":
        reminder = f"Medium priority task: {task}"
    case "low":
        reminder = f"Low priority task: {task}"
    case _:
        reminder = f"Task: {task} (Unknown priority)"

if time_bound.lower() == "yes":
    reminder += " that requires immediate attention today!"

# Provide a Customized Reminder
print(reminder)

