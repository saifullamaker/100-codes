# Problem 71: Program to convert a decimal number entered by the user
# into its binary equivalent, without using the built-in bin() function.

decimal_number = int(input("Enter a decimal number: "))

if decimal_number == 0:
    binary_number = "0"
else:
    temp = decimal_number
    binary_digits = []
    while temp > 0:
        remainder = temp % 2
        binary_digits.append(str(remainder))
        temp = temp // 2
    binary_digits.reverse()
    binary_number = "".join(binary_digits)

print("Binary equivalent of", decimal_number, "is:", binary_number)
