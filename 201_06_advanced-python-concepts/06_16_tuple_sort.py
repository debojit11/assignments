# Use a lambda expression to sort a list of tuples based on
# the number value in the tuple. For example:
#
# unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
# sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
# Sorting the list of tuples based on the second element in each tuple
sorted_list = sorted(unsorted_list, key=lambda x: x[1])

# Printing the sorted list
print(sorted_list)
