# 1. Ask the user to type a number
# input() reads whatever the user types as text (a string)
user_input = input("Enter a number to reverse: ")

# 2. Flip the text backward using [::-1]
reversed_text = user_input[::-1]

# 3. Print the result
print("The reversed number is:", reversed_text)
