# Write a script that prints out all the squares of numbers from 1 to 50.
# Use a `for` loop that demonstrates the use of the `range()` function.

result = 0

for i in range(1,51):
    result = i ** 2
    print(f"The square of {i} is {result}")
