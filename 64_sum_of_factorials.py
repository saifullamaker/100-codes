# Problem 64: Program to find the sum of factorials of the first n
# natural numbers, that is 1! + 2! + 3! + ... + n!.

n = int(input("Enter the value of n: "))

sum_of_factorials = 0

for number in range(1, n + 1):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    sum_of_factorials = sum_of_factorials + factorial

print("Sum of factorials from 1! to", str(n) + "! is:", sum_of_factorials)
