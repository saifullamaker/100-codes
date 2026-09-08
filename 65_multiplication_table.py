# Problem 65: Program to print the multiplication table of a number
# entered by the user, up to 10 terms.

number = int(input("Enter a number: "))

print("Multiplication table of", number)

for i in range(1, 11):
    product = number * i
    print(number, "x", i, "=", product)
