# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"
print(f"file_1: {file_1.endswith('.pdf')}")
print(f"file_2: {file_2.endswith('.pdf')}")
print(f"file_3: {file_3.endswith('.pdf')}")
print(f"file_4: {file_4.endswith('.pdf')}")
