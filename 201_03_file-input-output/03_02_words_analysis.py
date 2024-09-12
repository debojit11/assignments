# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

# Define the path to the words.txt file
file_path = "C:/Users/91763/Documents/codingnomads/python-201-main/python-201-main/201_03_file-input-output/words.txt"

# Initialize variables to store shortest, longest words and total count
shortest_words = []
longest_words = []
total_words = 0
shortest_length = float('inf')  # Start with a very large value
longest_length = 0  # Start with a small value

# Open and process the file
with open(file_path, "r") as file:
    for line in file:
        word = line.strip()  # Remove any leading/trailing whitespace
        total_words += 1
        
        # Check if the current word is the shortest
        if len(word) < shortest_length:
            shortest_words = [word]
            shortest_length = len(word)
        elif len(word) == shortest_length:
            shortest_words.append(word)
        
        # Check if the current word is the longest
        if len(word) > longest_length:
            longest_words = [word]
            longest_length = len(word)
        elif len(word) == longest_length:
            longest_words.append(word)

# Print the results
print(f"Shortest word(s) ({shortest_length} characters): {shortest_words}")
print(f"Longest word(s) ({longest_length} characters): {longest_words}")
print(f"Total number of words: {total_words}")