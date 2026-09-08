# Problem 73: Program to read numbers entered by the user until -1 is
# entered, then display the count of numbers entered and their average.
# (-1 itself is not included in the count or the average.)

count = 0
total = 0

print("Enter numbers one by one. Enter -1 to stop.")

while True:
    number = float(input("Enter a number: "))
    if number == -1:
        break
    total = total + number
    count = count + 1

if count == 0:
    print("No numbers were entered.")
else:
    average = total / count
    print("Count of numbers entered:", count)
    print("Average of numbers entered:", average)
