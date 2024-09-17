# Write a dictionary comprehension that maps each integer
# between `0` and `999` to a list of the digits that represents
# that integer in base 10. That is, your output should be:
#
# {0: [0], 1: [1], 2: [2], 3: [3], ...,
# 10: [1, 0], 11: [1, 1], 12: [1, 2], ...,
# 999: [9, 9, 9]}
#
# CHALLENGE: Write another dictionary comprehension that works the same
# but for base 2 (binary)! The output values should be:
#
# {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 1, 0], 3: [0, 1, 1], ...,
# 7: [1, 1, 1], 8: [1, 0, 0, 0], 9: [1, 0, 0, 1], ...,
# 999: [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]}

base10_dict = {i: [int(digit) for digit in str(i)] for i in range(1000)}
print(base10_dict)

base2_dict = {i: [int(bit) for bit in f'{i:0{len(bin(999))-2}b}'] for i in range(1000)}
print(base2_dict)
