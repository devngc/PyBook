def checkDiscount(product, discount):
    salePrice = product["price"] - (product['price'] * discount)
    message = "The sale price must be\
                                              greater than 0 and\
                                              less than the original\
                                              price of the product."
    assert 0 <= salePrice <= product['price'][message]
    return salePrice


store = {"name": "shoes", "price": 50}

print checkDiscount(store, 3.0)
