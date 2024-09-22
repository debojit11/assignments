# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?
#1
first_integer = 1
first_integer = float(first_integer)
print(type(first_integer), first_integer)

#2
second_float = 1.0
second_float = int(second_float)
print(type(second_float), second_float)

#3
float_num= 5.0
int_num= 2
result = float_num/int_num
print(result)

#4
a = 2
b = 3
product = a*b
print(product)

# precision is lost during division of float and int
