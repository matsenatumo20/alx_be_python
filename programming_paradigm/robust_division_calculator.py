def safe_divide(numerator, denominator):

    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        print("Error: Both numerator and denominator must be numeric.")
        return None
    
    try:
        quotient = numerator / denominator
        return quotient 
    except ZeroDivisionError:
        print("Error: Division by zero is undefined")
        return None
