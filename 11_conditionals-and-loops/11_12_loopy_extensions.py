# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"
is_pdf = True
if len(filename) < 4:
    is_pdf = False

for i in range(-4, 0):
    if filename[i] == ".pdf"[i + 4]:
        for i in range(-3, 0):
            if filename[i] != "pdf"[i + 3]:
                is_pdf = False
                break
if is_pdf:
    print("The file is a .pdf file.")
else:
    print("The file is not a .pdf file.")