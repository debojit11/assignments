# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    def __init__(self, name, radius, color, gravity):
        self.name = name
        self.radius = radius
        self.color = color
        self.gravity = gravity

    def __str__(self):
        return f"Planet: {self.name}\nRadius: {self.radius} km\nColor: {self.color}\nGravity: {self.gravity}m/s^2"

a = Planet("earth",6537, "blue",9.8) 
print(a)
