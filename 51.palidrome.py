# 1. Pick a number to check
original_number = 121
number = original_number  # Make a copy to work with
reversed_number = 0

# 2. Reverse the number mathematically
while number > 0:
    last_digit = number % 10
    reversed_number = (reversed_number * 10) + last_digit
    number = number // 10

# 3. Check if it matches the original
if original_number == reversed_number:
    print(original_number, "is a palindrome!")
else:
    print(original_number, "is NOT a palindrome.")
    
    
