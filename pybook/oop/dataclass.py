"""This module shows the use of dataclass. This works with python 3.7+"""

from dataclasses import dataclass, field
import random


def price_range():
    return random.randrange(20, 40)


@dataclass
class Book():
    """dataclass automatically implements __eq__ and __repr__ methods."""
    # Here we're defining attributes with type hints and default values.
    title: str = "No title"
    author: str = "No author"
    pages: int = field(default=0)
    price: float = field(default_factory=price_range)

    def __post_init__(self):
        """This magic method only works with dataclass. It helps to add attributes
        after an object of this class is created. """
        self.description = f'This useless book {self.title} by {self.author} is famous.'

    def book_info(self):
        return f'This book is {self.title} by {self.author}.'


b1 = Book("The three", "Crazy one", 132, 25)
print(b1)
print(b1.book_info())
print(b1.description)

b2 = Book()
print(b2)