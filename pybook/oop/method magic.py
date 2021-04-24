"""This script demonstrates the use of magic methods (Dunder methods).
More of such methods can be found in the Data model of Python documentation."""


class Book():
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self, val):
        """Checks equality between objects."""
        if not isinstance(val, Book):
            raise ValueError('{} is not a Book.'.format(val))
        else:
            return (
                self.title == val.title and
                self.author == val.author and
                self.price == val.price)

    def __ge__(self, val):
        """Checks if one objects is greater than another."""
        if not isinstance(val, Book):
            raise ValueError('{} is not a Book.'.format(val))
        else:
            return self.price >= val.price

    def __lt__(self, val):
        """Checks if one object is less than another."""
        if not isinstance(val, Book):
            raise ValueError('{} is not a Book.'.format(val))
        else:
            return self.price < val.price

    def __getattribute__(self, name):
        """This method is used when an attribute is requested."""
        if name == 'price':
            p = super().__getattribute__('price')
            return f'The price is {p}'

    def __getattr__(self, name):
        """This method is used when the above method is not defined."""
        return f'{name} prop is not found.'

    def __setattr__(self, name, value):
        """This method is used when an attribute is setup."""
        if name == 'price':
            if not isinstance(value, float):
                raise ValueError(f'{name} must be a float.')
            else:
                return super().__setattr__(name, value)


b1 = Book('The last three', 'Holy dogginess', 29.99)
b2 = Book('The good wives', 'Smart prince', 39.99)
b3 = Book('The last three', 'Holy dogginess', 29.99)

# The following equality check would be False if the the __eq__ magic method was not
# defined
print(b1 > b3)
print(b1 < b2)

# Since we implemented the magic methods, the objects can be sorted
books = [b1, b2, b3]
books.sort()
print([book.price for book in books])

# The following should throw an error
b2.price = 32
print(b2)