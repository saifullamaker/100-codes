"""
Problem 33: Ascending Order of Three Numbers
Statement: Given 3 numbers, print them in ascending order using only if-else
"""

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a <= b and a <= c:
    smallest = a
    if b <= c:
        middle, largest = b, c
    else:
        middle, largest = c, b
elif b <= a and b <= c:
    smallest = b
    if a <= c:
        middle, largest = a, c
    else:
        middle, largest = c, a
else:
    smallest = c
    if a <= b:
        middle, largest = a, b
    else:
        middle, largest = b, a

print("Ascending order:", smallest, middle, largest)
