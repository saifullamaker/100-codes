# Problem 66: Program to find the sum of even numbers and the sum of odd
# numbers from 1 to n, where n is entered by the user.

n = int(input("Enter the value of n: "))

sum_of_even = 0
sum_of_odd = 0

for number in range(1, n + 1):
    if number % 2 == 0:
        sum_of_even = sum_of_even + number
    else:
        sum_of_odd = sum_of_odd + number

print("Sum of even numbers from 1 to", n, "is:", sum_of_even)
print("Sum of odd numbers from 1 to", n, "is:", sum_of_odd)
