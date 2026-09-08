# Problem 61: Program to find the sum of the harmonic series
# 1 + 1/2 + 1/3 + ... + 1/n for a number n entered by the user.

n = int(input("Enter the value of n: "))

harmonic_sum = 0.0

for term in range(1, n + 1):
    harmonic_sum = harmonic_sum + (1 / term)

print("Sum of harmonic series up to", n, "terms is:", harmonic_sum)
