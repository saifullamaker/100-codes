"""
Problem 20: Vowel or Consonant
Statement: Check if a character is a vowel or consonant
"""

ch = input("Enter a single alphabet character: ")
ch_lower = ch.lower()

if ch_lower in ('a', 'e', 'i', 'o', 'u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")
