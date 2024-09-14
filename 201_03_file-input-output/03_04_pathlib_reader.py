# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

from pathlib import Path
import csv
from pprint import pprint

# Define the path to the CSV file using pathlib
file_path = Path("C:/Users/91763/Documents/codingnomads/python-201-main/python-201-main/201_03_file-input-output/file-counter/filecounts.csv")

# Initialize a dictionary to count file types
file_type_counts = {}

# Read the CSV file using the 'with' statement
with file_path.open('r') as file:
    reader = csv.reader(file)
    for row in reader:
        for ext in row:
            ext = ext.strip()  # Clean up whitespace
            if ext in file_type_counts:
                file_type_counts[ext] += 1
            else:
                file_type_counts[ext] = 1

# Pretty print the file type counts
print("File Type Counts from CSV:")
pprint(file_type_counts)


csv_file_path = Path("C:/Users/91763/Documents/codingnomads/python-201-main/python-201-main/201_03_file-input-output/file-counter/filecounts.csv")

# Define the count dictionary
count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

# Write the file counts to the CSV file using the 'with' statement
with csv_file_path.open("a", newline='') as csvfile:
    countwriter = csv.writer(csvfile)
    # Convert the dictionary values to a list
    data = [count.get("", 0), count.get(".csv", 0), count.get(".md", 0), count.get(".png", 0)]
    countwriter.writerow(data)