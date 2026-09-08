# Problem 77: Program to print numbers from 1 to n and then back from
# n to 1, using recursion.


def print_increasing_decreasing(current_number, n):
    # Base case: stop when current_number crosses n
    if current_number > n:
        return
    print(current_number, end=" ")
    # Recursive call to print the next increasing number
    print_increasing_decreasing(current_number + 1, n)
    # Print the current number again while returning from recursion
    print(current_number, end=" ")


n = int(input("Enter a positive number n: "))

print("Increasing then decreasing sequence:")
print_increasing_decreasing(1, n)
print()
