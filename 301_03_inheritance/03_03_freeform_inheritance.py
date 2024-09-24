# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"Vroom!"

    def __str__(self):
        return f"Vehicle: {self.year} {self.make} {self.model}"

class Truck(Vehicle):
    def __init__(self, make, model, year, bed_size):
        super().__init__(make, model, year)
        self.bed_size = bed_size

    def load_cargo(self, load):
        return f"Loading {load} into the {self.bed_size} bed of the {self.make} {self.model}."

    def __str__(self):
        return f"Truck: {self.year} {self.make} {self.model}, Bed Size: {self.bed_size}"

class Pickuptruck(Truck):
    def __init__(self, make, model, year, bed_size, towing_capacity):
        super().__init__(make, model, year, bed_size)
        self.towing_capacity = towing_capacity

    def tow(self, weight):
        if weight <= self.towing_capacity:
            return f"The {self.make} {self.model} is towing {weight} lbs."
        else:
            return f"The {self.make} {self.model} cannot tow more than {self.towing_capacity} lbs."

    def __str__(self):
        return f"Pickup Truck: {self.year} {self.make} {self.model}, Bed Size: {self.bed_size}, Towing Capacity: {self.towing_capacity} lbs"


if __name__ == '__main__':
    # Create instances of each class
    generic_vehicle = Vehicle("Generic", "Vehicle", 2020)
    ford_truck = Truck("Ford", "F-150", 2022, "large")
    toyota_pickup = Pickuptruck("Toyota", "Tacoma", 2023, "medium", 6500)

    # Demonstrate functionality
    print(generic_vehicle)
    print(generic_vehicle.start_engine())

    print(ford_truck)
    print(ford_truck.load_cargo("furniture"))

    print(toyota_pickup)
    print(toyota_pickup.tow(5000))
    print(toyota_pickup.tow(7000))  # Exceeds towing capacity    