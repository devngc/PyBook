"""This module shows the use of a decorator."""


def boss_coming(func):

    def wrapper():
        result = func()
        result += ' is coming!'
        return result
    return wrapper


@boss_coming
def call_boss():
    return 'DOG'


print(call_boss())
