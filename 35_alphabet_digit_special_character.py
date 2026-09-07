"""
Problem 35: Alphabet Digit Special Character
Statement: Check if a given character is an alphabet, digit, or special character
"""

ch = input("Enter a single character: ")

if ch.isalpha():
    print(ch, "is an Alphabet")
elif ch.isdigit():
    print(ch, "is a Digit")
else:
    print(ch, "is a Special Character")
