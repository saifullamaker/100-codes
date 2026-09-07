"""
Problem 22: Age Category
Statement: Age Category: Classify a person as child, teenager, adult, or senior based on age
"""

age = int(input("Enter age: "))

if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior Citizen"

print("Age category:", category)
