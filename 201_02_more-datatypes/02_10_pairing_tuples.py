# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here
sorted_list = sorted(randlist)

# Initialize an empty list to store the tuples
tuple_list = []

# Create tuples of two elements
for i in range(0, len(sorted_list), 2):
    # If there's a next item, create a tuple of two items
    if i + 1 < len(sorted_list):
        tuple_list.append((sorted_list[i], sorted_list[i + 1]))
    else:
        # Otherwise, pair the last item with 0
        tuple_list.append((sorted_list[i], 0))

# Print each tuple
for t in tuple_list:
    print(t)