a = int(input("First number: "))
b = int(input("Second number: "))

# Keep copies of original numbers to calculate LCM later
num1, num2 = a, b

# 1. Find the GCD first
while b != 0:
    a, b = b, a % b
gcd = a

# 2. Use the formula to find LCM
lcm = (num1 * num2) // gcd

print("LCM is:", lcm)
