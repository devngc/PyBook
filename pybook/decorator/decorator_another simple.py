"""This module shows the use of a decorator with arguments."""
from time import perf_counter
from functools import wraps


def duration(func):
    """Decorator function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """This is a wrapper function."""
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        print(f'It took {duration}')
        return result
    return wrapper


@duration
def add_me(*args, **kwargs):
    """Return sum of numebers."""
    return sum(args) + sum(kwargs.values())

print(add_me(1, 2, 4, 5,2.3, a=66.6))