def munch(start, end):
    def do_munch(func):
        def wrapper(*args, **kwargs):
            new_string = ''
            result = func()
            for index, char in enumerate (result):
                if start <= index <= end:
                    char = 'x'
                new_string += char
            return new_string
        return wrapper
    return do_munch


@munch(0, 44)
def pfib():
    return 'Fibonnaci'


print(pfib())