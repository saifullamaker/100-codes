"""
Problem 2: Area of Circle
Statement: Calculate the area of a circle given radius (A = pi * r^2)
"""

import math

radius = float(input("Enter the radius of the circle: "))

# Formula: A = pi * r^2
area = math.pi * radius ** 2

print("Area of the circle is:", round(area, 2))
