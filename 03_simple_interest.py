"""
Problem 3: Simple Interest
Statement: Calculate simple interest given P, R, T -> (P x R x T) / 100
"""

principal = float(input("Enter the Principal amount (P): "))
rate = float(input("Enter the Rate of interest (R): "))
time = float(input("Enter the Time in years (T): "))

# Formula: SI = (P x R x T) / 100
simple_interest = (principal * rate * time) / 100

print("Simple Interest is:", simple_interest)
