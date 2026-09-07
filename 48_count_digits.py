"""
Problem 48: Count Number of Digits
Statement: Count the number of digits in a number
"""

num = int(input("Enter a number: "))

original = num
num = abs(num)  # Handle negative numbers
count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num //= 10

print("Number of digits in", original, "is:", count)
