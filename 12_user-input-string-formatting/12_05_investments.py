# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.


investment_amount = float(input("Enter the investment amount: "))
interest_rate = float(input("Enter the interest rate (in percentage): "))
number_of_years = int(input("Enter the number of years to invest: "))

future_value = investment_amount * (1 + (interest_rate / 100)) ** number_of_years

print(f"The future value of the investment after {number_of_years} years is: {future_value:.2f}")
