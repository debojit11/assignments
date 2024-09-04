# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

user1 = input("Enter a opinion:")
output = ""
for i in range(len(user1)):
    char = user1[i]
    if char.isalpha():
        if i % 2 != 0:
            output += char.upper()
        else:
            output += char.lower()
    else:
        output += char
print(output)
