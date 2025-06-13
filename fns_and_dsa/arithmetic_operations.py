def perform_operation(num1: float, num2: float, operation: str) -> float:

    
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 != 0:
                return "Error, cannot divide by zero"
            else:
                return num1 / num2
        case _:
            return "Error: Invalid operation. Supported operations are 'add', 'subtract', 'multiply', and 'divide'."
