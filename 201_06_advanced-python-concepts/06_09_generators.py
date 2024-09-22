# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.

# A simple generator function that yields numbers from 0 to 4
def number_generator():
    for i in range(5):
        yield i  # Use yield instead of return

# Create a generator object
gen = number_generator()

# Print the generator object
print(gen)  # This will print the generator object

# Iterate over the generator and print each item
for num in gen:
    print(num)
