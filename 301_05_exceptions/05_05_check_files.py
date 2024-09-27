# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = r'C:/Users/91763/Documents/codingnomads/python-301-main/python-301-main/301_05_exceptions/integers.txt'

try:
    # Attempt to open the file and read the first number
    with open(file_name, 'r') as file:
        first_number = int(file.readline().strip())  # Read and convert to integer
except IOError:
    print("Error: Unable to read the file. Please check the file path and try again.")
except ValueError:
    print("Error: The file does not contain valid integers.")
else:
    # Perform a calculation with the first number if no exceptions occurred
    calculation_result = first_number * 2  # Example calculation (doubling the number)
    print(f"The first number is: {first_number}")
    print(f"The result of the calculation (first number * 2) is: {calculation_result}")

