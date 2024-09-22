# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

n = int(input("Enter a number: "))
result= {}

for num in range(1, n+1):
    result[num] = num * num
print(result)    