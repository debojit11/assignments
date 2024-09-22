# Use the `csv` module to read in and count the different file types.


# Define the path to the file

file_path = "C:/Users/91763/Documents/codingnomads/python-201-main/python-201-main/201_03_file-input-output/file-counter/filecounts.csv"
# Use the 'with' statement to open the file
with open(file_path, 'r') as file:
    # Read the content of the file
    content = file.read()
    print(content)



