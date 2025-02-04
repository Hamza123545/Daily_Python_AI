import math

def calculator():
    print("\nAdvanced Calculator")
    try:
        print("Operations: +, -, *, /, ^ (power), sqrt (square root), log (logarithm), sin, cos, tan")
        operation = input("Enter operation: ")
        
        if operation in ["+", "-", "*", "/", "^"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
            elif operation == "^":
                result = math.pow(num1, num2)
        
        elif operation == "sqrt":
            num = float(input("Enter number: "))
            result = math.sqrt(num)
        
        elif operation == "log":
            num = float(input("Enter number: "))
            result = math.log(num)
        
        elif operation in ["sin", "cos", "tan"]:
            num = float(input("Enter angle in degrees: "))
            radians = math.radians(num)
            if operation == "sin":
                result = math.sin(radians)
            elif operation == "cos":
                result = math.cos(radians)
            elif operation == "tan":
                result = math.tan(radians)
        
        else:
            result = "Invalid operation"
        
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
