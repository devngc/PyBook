"""This script demostrates how to use assert to check errors of your code
that is not going to be captured in a try - except clause"""


def checkDiscount(product, discount):
    salePrice = product["price"] - (product['price'] * discount)
    assert 0 <= salePrice <= product['price']
    return salePrice


store = {"name": "shoes", "price": 50}

print checkDiscount(store, 2.0)
