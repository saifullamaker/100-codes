num = int(input("Enter a number: "))

# Unhappy numbers always get stuck in a loop containing the number 4
while num != 1 and num != 4:
    # Sum the squares of the digits
    num = sum(int(digit) ** 2 for digit in str(num))

if num == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")
