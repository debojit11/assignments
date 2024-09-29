def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    if not numbers:
        raise ValueError("The list is empty, cannot calculate average.")
    return sum(numbers) / len(numbers)