# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

user1 = int(input("Enter a number between 0 and 1,000,000,000: "))
i = 0
while i <= 1000000000:
    if i == user1:
        print(f"Number found: {i}")
        break
    i += 1