"""This script demonstrates the use of magic method Call.
This method id useful if the atrributes of the objects are regularly updated."""


class Book():
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __call__(self, title, author, price):
        """Checks equality between objects."""
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"The book {self.title} by {self.author} unnecessarily costs {self.price}."


b1 = Book("Dogs were gods", "sooty dog", 129.99)
print(b1)
b1("Cats were nothing", "doggy cat", 239.99)
print(b1)
