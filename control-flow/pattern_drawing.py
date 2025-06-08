"""
pattern_drawing.py

Objective:
    Utilize while loops and nested for loops to draw a simple text-based pattern.

Task Description:
    This script prompts the user to enter a positive integer, then uses nested loops
    to print a square pattern of that size made of asterisks (*).

Instructions:
    1. Prompt User for Pattern Size:
        Ask the user to input a positive integer that represents the size of the pattern.
    2. Draw the Pattern:
        Use a while loop to iterate through each row of the pattern.
        Inside the while loop, use a for loop to print asterisks (*) side by side.
        After completing each row, print a newline character to move to the next row.

Usage:
    Run the script and enter a positive integer when prompted.
    The script will print a square pattern of the specified size made of asterisks (*).
"""
#My solution is here

size = int(input("Enter the size of the pattern: "))

while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row +=  1
