"""This module shows the ternary operator"""


def ternary_operator(val: bool) -> str:
    """A function to show the use of ternary operator in Python.

    Args:
        val: A boolean

    Returns:
        A string
    """
    x = "Feed the bear" if val else "Do not feed the bear"
    return x


print(ternary_operator("dd"))