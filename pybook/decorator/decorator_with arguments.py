"""This module shows how arguments can be passed to a decorator."""


def munch(start, end):
    """Replace letters of a string between index start and end with an 'x'.

    Args:
        start: An integer
        end: An integer
    """
    def do_munch(func):
        """Apply munch as a decorator on a function that returns a string.

        Args:
            func: A python function object that returns a string.
        """
        def wrapper(*args, **kwargs):
            new_string = ''
            result = func()
            for index, char in enumerate(result):
                if start <= index <= end:
                    char = 'x'
                new_string += char
            return new_string
        return wrapper
    return do_munch


@munch(0, 4)
def pfib():
    return 'Fibonnaci'


print(pfib())
