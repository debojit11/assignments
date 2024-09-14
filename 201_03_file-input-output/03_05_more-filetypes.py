# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.
from pathlib import Path
import csv

# Define the path to the Documents directory
documents_path = Path("/Users/91763/Documents")

# Define the path to the CSV file
csv_file_path = Path("C:/Users/91763/Documents/codingnomads/python-201-main/python-201-main/201_03_file-input-output/file-counter/filecounts.csv")

# Define the file types to count
file_types_to_count = {".pdf", ".jpg", ".txt", ".png", ".py"}

# Initialize a dictionary to count file types
file_type_counts = {ft: 0 for ft in file_types_to_count}

# Iterate through all files in the Documents directory and its subdirectories
for file in documents_path.rglob('*'):
    if file.is_file():
        # Get the file extension (e.g., '.png', '.txt')
        ext = file.suffix.lower()
        # Update the count for this extension if it's in the specified types
        if ext in file_type_counts:
            file_type_counts[ext] += 1

# Pretty print the file type counts
print("File Type Counts on Documents:")
for ext, count in file_type_counts.items():
    print(f"{ext}: {count}")

# Write the file counts to a CSV file
with csv_file_path.open("w", newline='') as csvfile:
    countwriter = csv.writer(csvfile)
    # Write header
    countwriter.writerow(["File Type", "Count"])
    # Write counts
    for ext, count in file_type_counts.items():
        countwriter.writerow([ext, count])