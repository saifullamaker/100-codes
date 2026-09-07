"""
Problem 29: Valid Triangle Check
Statement: Given 3 sides, check if a valid triangle can be formed
"""

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Triangle inequality theorem: sum of any two sides must be greater than the third
if (a + b > c) and (b + c > a) and (a + c > b):
    print("A valid triangle can be formed")
else:
    print("A valid triangle cannot be formed")
