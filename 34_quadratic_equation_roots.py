"""
Problem 34: Roots of Quadratic Equation
Statement: Find the roots of a quadratic equation (check discriminant: real, equal, imaginary)
"""

import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Roots are real and different")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif discriminant == 0:
    root1 = -b / (2 * a)
    print("Roots are real and equal")
    print("Root:", root1)
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-discriminant) / (2 * a)
    print("Roots are imaginary")
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")
