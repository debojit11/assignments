# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.
user1 = int(input("enter a num between 1 and 12: "))
if 1 <= user1 <= 12:
    if user1 == 1:
        print("January")
    elif user1 == 2:
        print("February")
    elif user1 == 3:
        print("March")
    elif user1 == 4:
        print("April")
    elif user1 == 5:
        print("May")
    elif user1 == 6:
        print("June")
    elif user1 == 7:
        print("July")
    elif user1 == 8:
        print("August")
    elif user1 == 9:
        print("September")
    elif user1 == 10:
        print("October")
    elif user1 == 11:
        print("November")
    elif user1 == 12:
        print("December")
    else:
        print("Error")