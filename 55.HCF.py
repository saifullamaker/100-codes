a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Keep subtracting the smaller number from the larger number
while b:
    a, b = b, a % b

print("HCF is:", a)
