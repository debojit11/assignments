# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

print(randlist)
print(f'largest number in the list is {max(randlist)}')

product = 1
for num in randlist:
    product *= num
print(f'product of all of the numbers in the list is {product}')