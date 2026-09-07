"""
Problem 28: Triangle Type by Sides
Statement: Check if a triangle is equilateral, isosceles, or scalene given 3 sides
"""

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a == b == c:
    print("The triangle is Equilateral")
elif a == b or b == c or a == c:
    print("The triangle is Isosceles")
else:
    print("The triangle is Scalene")
