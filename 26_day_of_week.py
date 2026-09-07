"""
Problem 26: Day of the Week
Statement: Read a number (1-7) and print the corresponding day of the week
"""

day_num = int(input("Enter a number (1-7): "))

if day_num == 1:
    day = "Monday"
elif day_num == 2:
    day = "Tuesday"
elif day_num == 3:
    day = "Wednesday"
elif day_num == 4:
    day = "Thursday"
elif day_num == 5:
    day = "Friday"
elif day_num == 6:
    day = "Saturday"
elif day_num == 7:
    day = "Sunday"
else:
    day = "Invalid input"

print("Day:", day)
