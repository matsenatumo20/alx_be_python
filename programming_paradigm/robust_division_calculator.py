def safe_divide(numerator, denominator):

    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")
        return None
    
    try:
        quotient = numerator / denominator
        return quotient 
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None


if __name__ == "__main__":
    print(safe_divide(10, 2))  # Output: 5.0
    print(safe_divide(10, 0))  # Output: Error: Division by zero is undefined.
    print(safe_divide("ten", 2))  # Output: Error: Both numerator and denominator must be numeric.
