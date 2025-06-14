def perform_operation(num1, num2, operation):
    """
    Performs a basic arithmetic operation based on the operation parameter.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform. Can be 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float: The result of the arithmetic operation. If division by zero occurs, returns "Error: Division by zero is not allowed."
    """
    # function implementation...
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2 
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error, cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation. Supported operations are 'add', 'subtract', 'multiply', and 'divide'."
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2 
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error, cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation. Supported operations are 'add', 'subtract', 'multiply', and 'divide'."
