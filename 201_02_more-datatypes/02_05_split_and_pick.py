# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

user = input("Enter a string: ")
words = list(user.split())
word_count = {}
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1    

common_word = ""
most_count = 0

for word, count in word_count.items():
    if count > most_count:
        common_word = word
        most_count = count

print(f"The most common word is: {common_word}")