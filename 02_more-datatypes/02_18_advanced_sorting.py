# CHALLENGE: Write a script that sorts a dictionary into a
# list of tuples based on the dictionary's values. For example:

# input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

# Check out the Python docs and see whether you can come up with a solution,
# even if you don't yet completely understand why it works the way it does:
# https://docs.python.org/3/howto/sorting.html#key-functions
# Feel free to discuss any questions you have with your mentor and on the forum!

# Create an empty dictionary
input_dict = {}

print("Enter dictionary items (type 'done' when finished):")

while True:
    key = input("Enter the key: ")
    if key.lower() == 'done':
        break
    value = input("Enter the value (numeric): ")
    
    # Ensure the value is numeric
    try:
        value = int(value)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        continue
    
    input_dict[key] = value

# Sort the dictionary by values and convert it to a list of tuples
sorted_list = sorted(input_dict.items(), key=lambda item: item[1])

# Print the sorted list of tuples
print("Sorted list of tuples by value:")
print(sorted_list)