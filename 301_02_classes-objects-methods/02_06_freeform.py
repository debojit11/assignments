# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

# Class 1: Book
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book: '{self.title}' by {self.author}, {self.pages} pages"

# Class 2: Phone
class Phone:
    def __init__(self, brand, model, memory_gb):
        self.brand = brand
        self.model = model
        self.memory_gb = memory_gb

    def __add__(self, other):
        """Overload the + operator to combine the memory of two phones."""
        combined_memory = self.memory_gb + other.memory_gb
        return Phone(self.brand, self.model + " + " + other.model, combined_memory)

    def __str__(self):
        return f"Phone: {self.brand} {self.model}, {self.memory_gb}GB memory"

# Class 3: Laptop
class Laptop:
    def __init__(self, brand, processor, ram_gb):
        self.brand = brand
        self.processor = processor
        self.ram_gb = ram_gb

    def __str__(self):
        return f"Laptop: {self.brand}, Processor: {self.processor}, RAM: {self.ram_gb}GB"

# Main script
if __name__ == '__main__':
    # Creating instances of Book
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
    book2 = Book("1984", "George Orwell", 328)

    # Creating instances of Phone
    phone1 = Phone("Apple", "iPhone 13", 128)
    phone2 = Phone("Samsung", "Galaxy S21", 256)

    # Creating instances of Laptop
    laptop1 = Laptop("Dell", "Intel i7", 16)
    laptop2 = Laptop("HP", "AMD Ryzen 5", 8)

    # Print out initial objects
    print(book1)
    print(book2)
    print(phone1)
    print(phone2)
    print(laptop1)
    print(laptop2)

    # Change some attributes
    phone1.memory_gb = 256  # Upgrading the memory of phone1
    book2.pages = 300  # Editing the number of pages of book2
    laptop1.ram_gb = 32  # Upgrading RAM of laptop1

    # Demonstrating overloaded __add__ method for Phone
    combined_phone = phone1 + phone2

    # Print updated objects
    print("\n--- Updated objects ---\n")
    print(phone1)
    print(book2)
    print(laptop1)

    # Print combined phone
    print("\n--- Combined Phone ---\n")
    print(combined_phone)