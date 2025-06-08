task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a {priority} priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a {priority} priority task"
    case "low":
        reminder = f"Note: '{task}' is a {priority} priority task"
    case _:
        reminder = f"Reminder: {task} (unknown priority)"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."

print(reminder)

      
      

