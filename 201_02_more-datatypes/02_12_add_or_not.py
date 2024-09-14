# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

# Initialize an empty set and set up the points
numbers = set()
points = 5

# Start the game loop
while True:
    # Get input from the user
    user_input = input("Enter a number: ")

    # Check if the input is a digit (ensures it's a number)
    if user_input.isdigit():
        num = int(user_input)

        # Check if the number is already in the set
        if num in numbers:
            print(f"{num} is a duplicate! You lose a point.")
            points -= 1
            print(f"You have {points} points left.")
        else:
            numbers.add(num)
            print(f"Added {num} to the set.")

        # Check for win condition
        if len(numbers) > 10:
            print("Congratulations, you win!")
            print(numbers)
            break

        # Check for loss condition
        if points <= 0:
            print("You've lost 5 points. Game over!")
            break
    else:
        print("Invalid input! Please enter a valid number.")
