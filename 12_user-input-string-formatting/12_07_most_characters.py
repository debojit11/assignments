# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

user1 = input("enter 1st string: ")
user2 = input("enter 2nd string: ")
user3 = input("enter 3rd string: ")
longest= max(user1, user2, user3, key=len)
print(f"The longest string is {longest}, and its length is {len(longest)}")