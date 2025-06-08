"""
daily_reminder.py

Task Description:
    This script asks the user for a single task, its priority level, and if it is time-sensitive.
    It then provides a customized reminder for that task, demonstrating control flow and loops.

Instructions:
    1. Prompt for a Single Task:
        - Ask the user to input a task description.
        - Prompt for the task's priority (high, medium, low).
        - Ask if the task is time-bound (yes or no).
    2. Process the Task Based on Priority and Time Sensitivity:
        - Use a match-case statement to react differently based on the task's priority.
        - Use an if statement to modify the reminder if the task is time-bound.
    3. Provide a Customized Reminder:
        - Print a reminder about the task that includes its priority level and whether immediate action is required.

Usage:
    Run the script and follow the prompts to enter a task, its priority, and time sensitivity.
    The script will provide a customized reminder based on your input.
"""
#My solution is here

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium priority task that requires no immediate attention, but you have to do it as soon as possible.")
    case "low":
        if time_bound == "no":
            print(f"{task} is a low priority task. Consider completing it when you have free time.")
