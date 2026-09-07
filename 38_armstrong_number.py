"""
Problem 38: Armstrong Number
Statement: Check if a 3-digit number is an Armstrong number (e.g., 153)
"""

num = int(input("Enter a 3-digit number: "))

original = num
total = 0

# Sum of cubes of each digit
while num > 0:
    digit = num % 10
    total += digit ** 3
    num //= 10

if total == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")
