"""
Problem 17: Leap Year Check
Statement: Check if a year is a leap year
"""

year = int(input("Enter a year: "))

# A year is leap if divisible by 4 and (not divisible by 100 or divisible by 400)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
