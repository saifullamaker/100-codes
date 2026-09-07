"""
Problem 5: Divisibility Check
Statement: Divisibility Check: Check whether a number is divisible by 3, 5, both, or neither
"""

num = int(input("Enter a number: "))

# Check divisibility using modulus operator
if num % 3 == 0 and num % 5 == 0:
    print(num, "is divisible by both 3 and 5")
elif num % 3 == 0:
    print(num, "is divisible by 3 only")
elif num % 5 == 0:
    print(num, "is divisible by 5 only")
else:
    print(num, "is not divisible by 3 or 5")
