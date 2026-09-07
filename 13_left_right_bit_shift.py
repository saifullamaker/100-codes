"""
Problem 13: Left Right Shift
Statement: Find the value of n << 1 and n >> 1 -- relate to multiply/divide by 2
"""

n = int(input("Enter a number: "))

left_shift = n << 1   # Left shift by 1 is same as multiplying by 2
right_shift = n >> 1  # Right shift by 1 is same as dividing by 2

print(f"{n} << 1 = {left_shift} (equivalent to {n} x 2)")
print(f"{n} >> 1 = {right_shift} (equivalent to {n} / 2, integer division)")
