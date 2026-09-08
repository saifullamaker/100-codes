# Problem 80: Program to print a right-aligned right-angled triangle
# pattern of stars using the number of rows entered by the user.
# Example for rows = 4:
#    *
#   **
#  ***
# ****

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * i
    print(spaces + stars)
