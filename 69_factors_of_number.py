# Problem 69: Program to display all the factors of a number entered
# by the user.

number = int(input("Enter a positive number: "))

print("Factors of", number, "are:")

for i in range(1, number + 1):
    if number % i == 0:
        print(i)
