# Problem 67: Program to check whether a number entered by the user is
# an Armstrong number or not.
# (An Armstrong number is a number that equals the sum of its own digits
# each raised to the power of the total number of digits.)

number = int(input("Enter a number: "))

original_number = number
number_of_digits = len(str(number))
sum_of_powers = 0

temp = number
while temp > 0:
    digit = temp % 10
    sum_of_powers = sum_of_powers + (digit ** number_of_digits)
    temp = temp // 10

if sum_of_powers == original_number:
    print(original_number, "is an Armstrong number.")
else:
    print(original_number, "is not an Armstrong number.")
