"""
multiplication_table.py

This script generates and prints the multiplication table for a given number.
It prompts the user to input a number and uses a for loop to calculate and print the multiplication table from 1 to 10.
"""
number = int(input("Enter a number to see its multiplication table: "))
 
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
