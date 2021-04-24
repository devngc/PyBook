"""This script shows the use of a secret attribute to a class."""


class Book():
    def __init__(self, title, author, pages, price):
        # The following are called instance attributes
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret property."\
            "Not to be accessed outside of this class"

    # The following functions are called instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    # This is creating an attribute
    def setdiscount(self, discount):
        # _ is used here to indicate to the developers that this is supposed to be an
        # internal attribute and should not be accessed from outside of the class.
        self._discount = discount


b1 = Book("Who said what", "bozo", 299, 39.99)
print(b1.getprice())
b1.setdiscount(0.1)
print(b1.getprice())

# Although not encouraged, you can access this attribute
print(b1._discount)
# See what happens when this attribute is called out
print(b1.__secret)
