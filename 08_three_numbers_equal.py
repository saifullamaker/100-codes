"""
Problem 8: Three Numbers Equal
Statement: Read three numbers and check if all three are equal (use &&)
"""

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Using logical AND (&&  ->  'and' in Python) to check equality
if a == b and b == c:
    print("All three numbers are equal")
else:
    print("The numbers are not all equal")
