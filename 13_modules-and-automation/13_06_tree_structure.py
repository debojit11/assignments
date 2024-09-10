# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
import pathlib

# Define the path to the folder
python_files_path = pathlib.Path('/Users/91763/Documents/codingnomads/python-101-main/python-101-main')

# Initialize a list to store the Python file paths
python_files = list(python_files_path.rglob('*.py'))

# Print header
print("Python files found:\n")

# Print each Python file with formatting
for filepath in python_files:
    print(f"- {filepath.relative_to(python_files_path)}")

# Print total count of Python files
print(f"\nTotal Python files found: {len(python_files)}")