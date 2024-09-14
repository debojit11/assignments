# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def print_advertisement_info(**kwargs):
    """
    Prints out nicely formatted information about a real estate advertisement.

    Args:
        **kwargs: Arbitrary keyword arguments representing advertisement details.
    """
    print("Real Estate Advertisement Information:")
    print("-" * 40)  # Print a line for better visual separation

    # Iterate over the keyword arguments and print each in a formatted manner
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

    print("-" * 40)  # Print a line for better visual separation

print_advertisement_info(
    location="123 Maple Street, Springfield",
    price="$350,000",
    bedrooms=3,
    bathrooms=2,
    square_feet=1800,
    features="Pool, Garage, Fireplace"
)