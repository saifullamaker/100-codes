# Problem 79: Program to print an inverted right-angled triangle pattern
# of stars using the number of rows entered by the user.
# Example for rows = 4:
# ****
# ***
# **
# *

rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    print("*" * i)
