"""
Problem 11: Even Odd Using Bitwise AND
Statement: Check if a number is even or odd using bitwise AND (n & 1)
"""

num = int(input("Enter a number: "))

# If the last bit is 1, the number is odd, else it is even
if num & 1 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
