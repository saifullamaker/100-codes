"""
Problem 39: Salary with Overtime
Statement: Given hours worked and rate, compute salary with overtime (>40 hrs at 1.5x rate)
"""

hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours > 40:
    regular_pay = 40 * rate
    overtime_pay = (hours - 40) * rate * 1.5
    salary = regular_pay + overtime_pay
else:
    salary = hours * rate

print("Total salary: Rs.", salary)
