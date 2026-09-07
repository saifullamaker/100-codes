"""
Problem 30: Simple Calculator
Statement: Build a simple calculator (+, -, x, /) using switch-case
"""

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Python does not have native switch-case (pre 3.10), so match-case is used
match operator:
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero")
    case _:
        print("Invalid operator")
