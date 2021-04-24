"""This script demonstrates the use of class method."""


class Book ():

    __BOOKTYPES = ('Hardcover', 'Ebook', 'Paperback')

    def __init__(self, title, book_type):
        self.title = title
        if book_type in Book.__BOOKTYPES:
            self.book_type = book_type
        else:
            raise AttributeError('{} is not a valid book type.'.format(book_type))

    @classmethod
    def get_book_types(cls):
        return cls.__BOOKTYPES

b1 = Book('The last three', 'Ebook')
print(b1.get_book_types())