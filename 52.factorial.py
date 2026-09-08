# 1. Get input from the user
num = int(input("Enter a number: "))

# 2. Calculate the factorial
fact = 1
while num > 1:
    fact *= num
    num -= 1

# 3. Print the answer
print(fact)
