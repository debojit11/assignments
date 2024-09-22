# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4
string_input = input("Enter a string: ")
letter_input = input("Enter a letter: ")
index = string_input.find(letter_input)
print(f"Index of first occurrence of the letter {letter_input} is {index}")