# Problem 72: Program to convert a binary number entered by the user
# (as a string of 0s and 1s) into its decimal equivalent, without using
# the built-in int(x, 2) conversion.

binary_number = input("Enter a binary number: ")

decimal_number = 0
power = 0

for digit in reversed(binary_number):
    if digit == "1":
        decimal_number = decimal_number + (2 ** power)
    power = power + 1

print("Decimal equivalent of", binary_number, "is:", decimal_number)
