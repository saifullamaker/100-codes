"""
Problem 27: Electricity Bill
Statement: Calculate electricity bill based on slab rates
"""

units = float(input("Enter number of units consumed: "))

# Simple slab rate calculation
if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = 100 * 3 + (units - 100) * 5
elif units <= 300:
    bill = 100 * 3 + 100 * 5 + (units - 200) * 7
else:
    bill = 100 * 3 + 100 * 5 + 100 * 7 + (units - 300) * 10

print("Electricity bill for", units, "units is: Rs.", round(bill, 2))
