"""
Problem 47: Sum of First N Natural Numbers
Statement: Calculate the sum of first N natural numbers
"""

n = int(input("Enter the value of N: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Sum of first", n, "natural numbers is:", total)
