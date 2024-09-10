# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please
string_input = input("Enter a string: ")
symbol = input("Enter a symbol: ")
result = ""
for word in string_input:
    if word == string_input[0]:
        result += symbol 
    else:
        result += word 
print(result)
