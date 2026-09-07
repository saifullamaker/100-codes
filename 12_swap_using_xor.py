"""
Problem 12: Swap Using XOR
Statement: Swap two numbers using XOR
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping: a =", a, " b =", b)

# Swapping using XOR bitwise operator
a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping: a =", a, " b =", b)
