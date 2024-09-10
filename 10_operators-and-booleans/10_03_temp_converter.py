# Fahrenheit to Celsius:
# ----------------------
# Write the necessary code to convert a degree in Fahrenheit
# to Celsius and print it to the console. Use variable names!
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")