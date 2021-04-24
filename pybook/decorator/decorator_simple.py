"""This module shows the use of a decorator."""
from functools import wraps


def boss_coming(func):
    """Decorator function"""
    # The wraps decorator makes sure that the docstrings are maintained
    # without this decorator an assertion error will be raised below as
    # the docstring of wrapper function will be assigned to the call_boss function
    @wraps(func)
    def wrapper():
        """This is a wrapper function"""
        result = func()
        result += ' is coming!'
        return result
    return wrapper


@boss_coming
def call_boss():
    """Calling boss!"""
    return 'DOG'


assert call_boss.__doc__ == 'Calling boss!'
