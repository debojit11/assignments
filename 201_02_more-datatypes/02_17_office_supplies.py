# Using f-strings, print out the name, last name, and favorite
# office supply item of each person in the given dictionary,
# formatted like so:
#
# LASTNAME, Name           Office supply item
# LONGERLASTNAME, Name     Office supply item

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]
max_lastname_length = max(len(person['full_name'].split()[-1]) for person in office)
max_firstname_length = max(len(person['full_name'].split()[0]) for person in office)
max_item_length = max(len(person['item']) for person in office)

# Define column widths
lastname_column_width = max_lastname_length + 2  # Add space for formatting
firstname_column_width = max_firstname_length + 2  # Add space for formatting
item_column_width = max_item_length + 2  # Add space for formatting

# Print each person's details
for person in office:
    full_name = person["full_name"]
    last_name, first_name = full_name.split()[-1], full_name.split()[0]
    item = person["item"]
    
    # Format the output
    print(f"{last_name.upper():<{lastname_column_width}} {first_name:<{firstname_column_width}} {item:<{item_column_width}}")


# I COULDN'T DO IT , TRIED FOR NEARLY 3 HOURS