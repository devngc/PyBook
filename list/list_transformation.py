nums = list(range(25))


def filter_odds(x):
    return True if x % 2 == 0 else False


def squared(x):
    return x ** 2


# Using the built in filter function
print(list(filter(filter_odds, nums)))

# Using map function
print(list(map(squared, nums)))

# Using lambda with Map
print(list(map(lambda x: x**2, nums)))
