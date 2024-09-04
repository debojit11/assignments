# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.
user_input= input("Enter a string: ")
a = 0
e = 0
i = 0
o = 0
u = 0
for char in user_input:
    if char.lower() == 'a':
        a += 1
    elif char.lower()== 'e':
        e += 1
    elif char.lower() == 'i':
        i += 1
    elif char.lower() == 'o':
        o += 1
    elif char.lower() == 'u':
        u += 1
print(f"a: {a}, e: {e}, i: {i}, o: {o}, u: {u}")