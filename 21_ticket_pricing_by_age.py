"""
Problem 21: Ticket Pricing
Statement: Ticket Pricing: Calculate ticket price based on the customer's age
"""

age = int(input("Enter customer's age: "))

# Simple age based ticket pricing rules
if age < 5:
    price = 0
elif age <= 12:
    price = 50
elif age <= 60:
    price = 100
else:
    price = 60  # senior citizen discount

print("Ticket price for age", age, "is: Rs.", price)
