"""
Problem 15: Count Set Bits
Statement: Count the number of set bits in a number
"""

num = int(input("Enter a number: "))

original = num
count = 0

# Loop until the number becomes 0, checking each bit
while num > 0:
    count += num & 1
    num = num >> 1

print(f"Number of set bits in {original} is: {count}")
