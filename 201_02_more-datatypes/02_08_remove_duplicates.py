# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

my_list = [1,2,3,4,5,6,6,5,4,3,2,1]
print(list(set(my_list)))



unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)