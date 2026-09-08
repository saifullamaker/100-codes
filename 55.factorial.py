# 1. Choose your number
n =int(input("enter your number:"))
fact = 1

# 2. Multiply and count downward
while n > 1:
    fact = fact * n
    n = n - 1    # Subtract 1 to move to the next lower number

# 3. Print the answer
print("The factorial is:", fact)
