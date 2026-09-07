"""
Problem 32: Sign and Even Odd Check
Statement: Check if a number is positive, negative, or zero -- then if positive check even/odd
"""

num = int(input("Enter a number: "))

if num > 0:
    print(num, "is Positive")
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")
elif num < 0:
    print(num, "is Negative")
else:
    print("The number is Zero")
