# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

# Keep prompting the user until they enter a valid integer
while True:
    user_input = input("Please enter an integer: ")
    
    try:
        # Attempt to convert the input to an integer
        user_integer = int(user_input)
        print(f"Thank you! You entered the integer: {user_integer}")
        break  # Exit the loop if the input is a valid integer
    except ValueError:
        # Handle the case where the input cannot be converted to an integer
        print("Invalid input. That's not an integer. Please try again.")
