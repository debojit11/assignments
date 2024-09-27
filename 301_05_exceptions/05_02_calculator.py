# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.

try:
    dividend = int(input("Please enter the number to be divided: "))
    divisor = int(input("Please enter the divisor: "))
    result = dividend / divisor
    print(f"The result of {dividend} divided by {divisor} is {result}")
except ZeroDivisionError:
    print("My most sincere apologies, but you can't divide by zero.")
except ValueError:
    print("I am once again asking you to use only digits in your input.")
except Exception as e:
    print(f"I humbly inform you that {e} has occurred.")