"""
Problem 6: Greater of Two Numbers
Statement: Read two numbers and print which is greater (use relational operators)
"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Using relational operator to compare
if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")
