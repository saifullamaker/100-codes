# Problem 75: Program to check whether a string entered by the user is
# a palindrome or not, using recursion.


def is_palindrome_recursive(text):
    # Base case: a string of length 0 or 1 is always a palindrome
    if len(text) <= 1:
        return True
    # If the first and last characters differ, it is not a palindrome
    if text[0] != text[-1]:
        return False
    # Recursive case: check the string without its first and last characters
    return is_palindrome_recursive(text[1:-1])


user_text = input("Enter a string: ")
cleaned_text = user_text.replace(" ", "").lower()

if is_palindrome_recursive(cleaned_text):
    print(user_text, "is a palindrome.")
else:
    print(user_text, "is not a palindrome.")
