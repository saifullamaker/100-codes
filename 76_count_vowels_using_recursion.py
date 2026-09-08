# Problem 76: Program to count the number of vowels in a string entered
# by the user, using recursion.


def count_vowels_recursive(text):
    vowels = "aeiouAEIOU"
    # Base case: an empty string has no vowels
    if len(text) == 0:
        return 0
    # Check the first character, then recurse on the rest of the string
    first_character_count = 1 if text[0] in vowels else 0
    return first_character_count + count_vowels_recursive(text[1:])


user_text = input("Enter a string: ")
vowel_count = count_vowels_recursive(user_text)

print("Number of vowels in the string:", vowel_count)
