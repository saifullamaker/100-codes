# Problem 74: Program to find the sum of the series
# x - x^2/2! + x^3/3! - x^4/4! + ... up to n terms,
# where x and n are entered by the user.

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))

series_sum = 0.0

for i in range(1, n + 1):
    term = x ** i
    factorial = 1
    for j in range(1, i + 1):
        factorial = factorial * j
    term = term / factorial

    if i % 2 == 0:
        series_sum = series_sum - term
    else:
        series_sum = series_sum + term

print("Sum of the series up to", n, "terms is:", series_sum)
