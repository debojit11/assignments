# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

# Define the path to the words.txt file
file_path = "C:/Users/91763/Documents/codingnomads/python-201-main/python-201-main/201_03_file-input-output/words.txt"
reverse_file_path = "C:/Users/91763/Documents/codingnomads/python-201-main/python-201-main/201_03_file-input-output/words_reverse.txt"

# Read the contents of words.txt
with open(file_path, "r") as file:
    content = file.readlines()

# Reverse the contents
reversed_content = content[::-1]

# Write the reversed contents to words_reverse.txt
with open(reverse_file_path, "w") as reverse_file:
    reverse_file.writelines(reversed_content)

print(f"Reversed content has been written to {reverse_file_path}")