"""
Problem 25: Grade Calculator
Statement: Given marks (0-100), print grade: A(>=90), B(>=80), C(>=70), D(>=60), F(<60)
"""

marks = float(input("Enter marks (0-100): "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
