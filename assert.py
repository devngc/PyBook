def checkDiscount(product, discount):
    salePrice = product["price"] - (product['price'] * discount)
    assert 0 <= salePrice <= product['price']
    return salePrice


store = {"name": "shoes", "price": 50}

print checkDiscount(store, 2.0)
