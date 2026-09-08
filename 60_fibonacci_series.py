# Problem 60: Program to print the Fibonacci series up to n terms
# entered by the user.

n = int(input("Enter the number of terms: "))

first_term = 0
second_term = 1

print("Fibonacci Series:")

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(first_term)
else:
    print(first_term, second_term, end=" ")
    for count in range(2, n):
        next_term = first_term + second_term
        print(next_term, end=" ")
        first_term = second_term
        second_term = next_term
    print()
