"""
Problem 37: Quadrant of a Point
Statement: Given coordinates (x, y), determine which quadrant the point lies in
"""

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x == 0 and y == 0:
    print("The point is at the Origin")
elif x == 0:
    print("The point lies on the Y-axis")
elif y == 0:
    print("The point lies on the X-axis")
elif x > 0 and y > 0:
    print("The point lies in Quadrant I")
elif x < 0 and y > 0:
    print("The point lies in Quadrant II")
elif x < 0 and y < 0:
    print("The point lies in Quadrant III")
else:
    print("The point lies in Quadrant IV")
