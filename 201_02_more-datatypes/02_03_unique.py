# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

list = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = []
for item in list:
    if list.count(item)==1:
        unique_list.append(item)
print(unique_list)