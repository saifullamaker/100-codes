# Problem 62: Program to find the alternating sum of the first n natural
# numbers, that is 1 - 2 + 3 - 4 + 5 - ... up to n terms.

n = int(input("Enter the value of n: "))

alternating_sum = 0

for number in range(1, n + 1):
    if number % 2 == 0:
        alternating_sum = alternating_sum - number
    else:
        alternating_sum = alternating_sum + number

print("Alternating sum up to", n, "is:", alternating_sum)
