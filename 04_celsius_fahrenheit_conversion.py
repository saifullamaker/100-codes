"""
Problem 4: Celsius Fahrenheit Conversion
Statement: Convert temperature from Celsius to Fahrenheit and vice versa
"""

choice = input("Convert from (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? ")

if choice.upper() == "C":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")
elif choice.upper() == "F":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")
else:
    print("Invalid choice entered")
