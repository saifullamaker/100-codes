"""
Problem 42: Scholarship Eligibility
Statement: Scholarship Eligibility: Determine eligibility based on marks, attendance, and family income
"""

marks = float(input("Enter marks percentage: "))
attendance = float(input("Enter attendance percentage: "))
family_income = float(input("Enter annual family income: "))

if marks >= 75 and attendance >= 80 and family_income <= 200000:
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")
