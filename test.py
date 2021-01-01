# /usr/bin/python3

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        self._discount = amount


b1 = Book("War", "Leo", 128, 332)
print(b1.get_price())