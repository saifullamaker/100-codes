# Problem 63: Program to find the power of a number (base ^ exponent)
# without using the built-in pow() function or ** operator.

base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent (whole number): "))

result = 1
is_negative_exponent = False

if exponent < 0:
    is_negative_exponent = True
    exponent = -exponent

for count in range(exponent):
    result = result * base

if is_negative_exponent:
    result = 1 / result

print("Result:", result)
