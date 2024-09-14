# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def divisible_by_4_or_7(number):
    """Check if a number is divisible by 4 or 7.

    Args:
        number (int): The number to check divisibility.

    Returns:
        bool: True if the number is divisible by 4 or 7, False otherwise.
    """
    return number % 4 == 0 or number % 7 == 0


def divisible_by_4_and_7(number):
    """Check if a number is divisible by both 4 and 7.

    Args:
        number (int): The number to check divisibility.

    Returns:
        bool: True if the number is divisible by both 4 and 7, False otherwise.
    """
    return number % 4 == 0 and number % 7 == 0


# Take user input within the range 1 to 1,000,000,000
user_input = int(input("Enter a number between 1 and 1,000,000,000: "))

if 1 <= user_input <= 1_000_000_000:
    # Call the functions and store the results
    result_or = divisible_by_4_or_7(user_input)
    result_and = divisible_by_4_and_7(user_input)

    # Print results with descriptive messages
    print(f"Is {user_input} divisible by 4 or 7? {result_or}")
    print(f"Is {user_input} divisible by both 4 and 7? {result_and}")
else:
    print("The number is out of the specified range.")