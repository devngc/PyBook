"""This module shows the use of immutable dataclass."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Book():
    """dataclass automatically implements __eq__ and __repr__ methods."""
    # Here we're defining attributes with type hints and default values.
    title: str = "No title"
    author: str = "No author"
    pages: int = 0
    price: float = 0


b1 = Book()
print(b1.title)
b1.title = "Who let the dogs out."

