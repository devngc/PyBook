"""One more example of inheritance."""


class Publication():
    def __init__(self, name, pages, price):
        self.name = name
        self.pages = pages
        self.price = price


class Company(Publication):
    def __init__(self, name, pages, price, publisher):
        super().__init__(name, pages, price)
        self.publisher = publisher


class Book(Publication):
    def __init__(self, name, pages, price, released, author):
        super().__init__(name, pages, price)
        self.released = released
        self.author = author


class Magazine(Company):
    def __init__(self, name, pages, price, publisher):
        super().__init__(name, pages, price, publisher)


class Newspaper(Company):
    def __init__(self, name, pages, price, publisher, frequency):
        super().__init__(name, pages, price, publisher)
        self.frequency = frequency


b1 = Book('The last three', 124, 22, '1998-03-22', 'Dickens')
print(b1.name)

m1 = Magazine('The cars', 25, 29.99, 'The dumb cars')
print(m1.price, m1.publisher)

n1 = Newspaper('The useless daily', 10, 2.95, 'The useless class', 'Every minute')
print(n1.pages, n1.frequency)