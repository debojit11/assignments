# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"
print(tuple(string))
print(list(tuple(string)))
list1 = list(tuple(string))
list1[0] = 'k'
print(tuple(list1))