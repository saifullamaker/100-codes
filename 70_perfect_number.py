# Problem 70: Program to check whether a number entered by the user is
# a perfect number or not.
# (A perfect number is a number that is equal to the sum of its
# positive divisors, excluding the number itself.)

number = int(input("Enter a positive number: "))

sum_of_divisors = 0

for i in range(1, number):
    if number % i == 0:
        sum_of_divisors = sum_of_divisors + i

if sum_of_divisors == number:
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")
