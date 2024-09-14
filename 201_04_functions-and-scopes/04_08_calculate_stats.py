# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(numbers):
    """Calculate and print the maximum, minimum, average, and sum of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        None
    """
    maximum = max(numbers)
    minimum = min(numbers)
    total_sum = sum(numbers)
    average = total_sum / len(numbers)

    # Print the results
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    print(f"Sum: {total_sum}")
    print(f"Average: {average}")
    return

# Example list to test the function
example_list = [1, 2, 3, 4, 5, 6, 7]

# Call the function
stats(example_list)