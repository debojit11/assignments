# Adapt your Generator expression from the previous exercise:
# Add a floor division by 1111 on it.
# What numbers do you get?

nums = range(1, 1000000)
# Create a generator that yields the result of floor division by 1111 for numbers divisible by 1111
gen = (num // 1111 for num in nums if num % 1111 == 0)

# Iterate over the generator and print each item
for num in gen:
    print(num)
