# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.
while True:
    user_input = int(input("Choose a number between 1 and 1,000,000,000: "))
    if 1<= user_input<= 1000000000:
        print("Checking if the number is divisible by 3")
        if user_input % 3 == 0:
            print(f"{user_input} is divisible by 3.")
        else:
            print(f"{user_input} is not divisible by 3.")
        break
    else:
        print("Please enter a number between 1 and 1,000,000,000")
