# 1. Get input as text
num_str = input("Enter a number: ")

# 2. Loop through each character, convert to integer, and multiply
product = 1
for digit in num_str:
    product *= int(digit)

# 3. Print the answer
print(product)
