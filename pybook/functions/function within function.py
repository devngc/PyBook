"""This module shows how a function within a function uses contexual arguments."""


def three_nums(a, b, c):

    def get_three():
        return a, b, c

    return get_three


f = three_nums(1, 2, 3)
print(f())
