# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).
# Define the path to the words.txt file
file_path = "C:/Users/91763/Documents/codingnomads/python-201-main/python-201-main/201_03_file-input-output/words.txt"

# Open the file and process it
with open(file_path, "r") as file:
    for line in file:
        word = line.strip()  # Remove any leading/trailing whitespace
        if len(word) > 20:  # Check if the word has more than 20 characters
            print(word)