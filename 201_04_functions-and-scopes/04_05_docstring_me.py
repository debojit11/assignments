# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """    Convert kilometers to miles.

    This function takes a distance in kilometers and converts it to miles
    using the conversion rate 1 kilometer = 0.6 miles.

    Args:
        km (float): The distance in kilometers.

    Returns:
        float: The equivalent distance in miles."""

    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
print(km_to_miles(1.7))