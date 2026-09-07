"""
Problem 31: Days in Month
Statement: Read month number (1-12) and print number of days in that month
"""

month = int(input("Enter month number (1-12): "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        days = 31
    case 4 | 6 | 9 | 11:
        days = 30
    case 2:
        days = 28  # Not considering leap year here
    case _:
        days = None

if days:
    print(f"Month {month} has {days} days")
else:
    print("Invalid month number")
