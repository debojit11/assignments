# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?


# Define the file paths using forward slashes
base_path = 'C:/Users/91763/Documents/codingnomads/python-301-main/python-301-main/301_05_exceptions/books'
war_and_peace_path = f'{base_path}/war_and_peace.txt'
pride_and_prejudice_path = f'{base_path}/pride_and_prejudice.txt'
crime_and_punishment_path = f'{base_path}/crime_and_punishment.txt'

# 1) Open war_and_peace.txt, read the whole file content and store it in a variable
try:
    with open(war_and_peace_path, 'r', encoding='utf-8') as file:
        war_and_peace_content = file.read()
except IOError:
    print("Error: Unable to read 'war_and_peace.txt'.")

# 2) Open crime_and_punishment.txt and overwrite the whole content with an empty string
try:
    with open(crime_and_punishment_path, 'w', encoding='utf-8') as file:
        file.write("")  # Overwriting with an empty string
except IOError:
    print("Error: Unable to write to 'crime_and_punishment.txt'.")

# 3) Loop over all three files and print out only the first character each
for book_path in [war_and_peace_path, pride_and_prejudice_path, crime_and_punishment_path]:
    try:
        with open(book_path, 'r', encoding='utf-8') as file:
            first_character = file.read(1)  # Read only the first character
            # Print the first character, or indicate that it is empty
            if first_character:
                print(f"The first character in {book_path.split('/')[-1]}: '{first_character}'")
            else:
                print(f"The first character in {book_path.split('/')[-1]}: ''")  # Print empty character
    except IOError:
        print(f"Error: Unable to read '{book_path.split('/')[-1]}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")