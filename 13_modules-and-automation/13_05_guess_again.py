# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random
guess = None
num = random.randint(1, 10)
tries = 0
max_tries = 10
while guess != num:
    guess = int(input("Guess a number between 1 and 10: "))
    tries += 1
    if guess == num:
        print("You guessed it!")
    else:
        if tries < max_tries:
            print(f"Try again! You have {max_tries - tries} tries left")
        else:
            print(f"You lost! The number was {num}")

