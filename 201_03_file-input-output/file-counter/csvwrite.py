# Write the file counts to a `.csv` file.
import csv
count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

with open("C:/Users/91763/Documents/codingnomads/python-201-main/python-201-main/201_03_file-input-output/file-counter/filecounts.csv", "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[""], count[".csv"], count[".md"], count[".png"]]
    countwriter.writerow(data)
