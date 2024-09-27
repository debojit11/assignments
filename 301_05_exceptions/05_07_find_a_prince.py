# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".


# Custom Exception Class
# Custom Exception Class
class PrinceException(Exception):
    """Exception raised when the first 100 characters of a book contain 'Prince'."""
    pass

# Define the file paths using forward slashes
base_path = 'C:/Users/91763/Documents/codingnomads/python-301-main/python-301-main/301_05_exceptions/books'
book_files = [
    f'{base_path}/war_and_peace.txt',
    f'{base_path}/pride_and_prejudice.txt',
    f'{base_path}/crime_and_punishment.txt'
]

# Loop over all book files
for book_path in book_files:
    try:
        # Open the book file and read the first 100 characters
        with open(book_path, 'r', encoding="utf-8") as file:
            content = file.read(100)  # Read first 100 characters
            
            # Check if "Prince" is in the content
            if "Prince" in content:
                raise PrinceException(f"'Prince' found in {book_path.split('/')[-1]}")
            else:
                print(f"No occurrence of 'Prince' in {book_path.split('/')[-1]}.")

    except PrinceException as pe:
        print(pe)  # Print the custom exception message
    except IOError:
        print(f"Error: Unable to read '{book_path.split('/')[-1]}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")