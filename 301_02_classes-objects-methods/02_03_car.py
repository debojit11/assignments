# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.
class Car:
    def __init__(self, model, year, max_speed):
        """Initialize the car with model, year, and max speed."""
        self.model = model
        self.year = year
        self.max_speed = max_speed  # max speed in km/h

    def increase_speed(self):
        """Increase the max speed of the car by 5 km/h."""
        self.max_speed += 5
        print(f"The max speed of the {self.model} has been increased to {self.max_speed} km/h.")

    def print_details(self):
        """Print the details of the car."""
        print(f"Car Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Max Speed: {self.max_speed} km/h")

# Creating objects of the Car class
car1 = Car("Toyota Corolla", 2020, 180)
car2 = Car("Honda Civic", 2021, 200)

# Printing details of both cars
car1.print_details()
car2.print_details()

# Increasing the max speed of both cars
car1.increase_speed()
car2.increase_speed()

# Printing updated details
print("\nUpdated Car Details:")
car1.print_details()
car2.print_details()
