# Assignment 1: Design Your Own Class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."

    def read(self):
        print(f"You are reading '{self.title}'. Enjoy the journey!")

# Inheritance: EBook adapts Book with an extra attribute
class EBook(Book):
    def __init__(self, title, author, pages, file_format):
        super().__init__(title, author, pages)
        self.file_format = file_format

    def description(self):
        base_desc = super().description()
        return f"{base_desc} Format: {self.file_format}."

    def read(self):
        print(f"Opening the {self.file_format} e-book '{self.title}' on your device!")

# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this!")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

def demonstrate_polymorphism(vehicles):
    for v in vehicles:
        v.move()

# Example usage
if __name__ == "__main__":
    # Test the Book class and inheritance
    physical_book = Book("1984", "George Orwell", 328)
    ebook = EBook("1984", "George Orwell", 328, "PDF")
    
    print(physical_book.description())
    physical_book.read()
    
    print(ebook.description())
    ebook.read()
    
    print("\nPolymorphism in action:")
    vehicles = [Car(), Plane(), Boat()]
    demonstrate_polymorphism(vehicles)
