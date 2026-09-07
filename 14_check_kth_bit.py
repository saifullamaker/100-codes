"""
Problem 14: Check Kth Bit
Statement: Check if the Kth bit of a number is set or not
"""

num = int(input("Enter a number: "))
k = int(input("Enter bit position (K) to check (0-indexed from right): "))

# Right shift num by k, then AND with 1
if (num >> k) & 1:
    print(f"Bit at position {k} is SET (1)")
else:
    print(f"Bit at position {k} is NOT SET (0)")
