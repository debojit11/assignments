# Create another child class that inherits from `Ingredient()`. You can use
# the code you wrote yourself, or continue working with the one provided below.
# Implement at least one extra method for your child class, and override the
# `expire()` method from the parent `Ingredient()` class.

class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient):
    """Models a spice to flavor your food."""

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "old " + self.name

    def add_dish(self, dish):
        """ adding the spice to a dish"""
        print(f"Adding {self.name} to {dish}.")

if __name__ == '__main__':
    ingredient = Ingredient("tomato", 5)
    spice = Spice("pepper", 2)
    
    print(ingredient)
    print(spice)
    
    spice.grind()
    spice.add_dish("pasta")
    spice.expire()
    print(spice)