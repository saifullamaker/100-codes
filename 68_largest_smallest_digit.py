# Problem 68: Program to find the largest and smallest digit in a
# number entered by the user.

number = int(input("Enter a number: "))

positive_number = abs(number)
temp = positive_number

largest_digit = temp % 10
smallest_digit = temp % 10
temp = temp // 10

while temp > 0:
    digit = temp % 10
    if digit > largest_digit:
        largest_digit = digit
    if digit < smallest_digit:
        smallest_digit = digit
    temp = temp // 10

print("Largest digit:", largest_digit)
print("Smallest digit:", smallest_digit)
