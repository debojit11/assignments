# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(bread, *args):
    """Make a sandwich with the given bread and toppings."""
    sandwich = bread + "\n" + "\n".join(args) + "\n" + bread
    return sandwich

print(make_sandwich("white bread", "cheese", "tomato", "lettuce"))