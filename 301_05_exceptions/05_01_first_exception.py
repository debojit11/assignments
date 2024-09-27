# Write a script that generates an exception.
# Handle this exception with a try/except block.
# For example:
#
# list_ = ["hello world!"]
# print(list_[1])
#
# This raises and exception that needs to be handled.

# A list with one element
list_ = ["hello world!"]

try:
    # Trying to access an index that does not exist
    print(list_[1])
except IndexError as e:
    # Handling the exception
    print(f"An IndexError occurred: {e}")