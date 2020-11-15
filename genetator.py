"""This script demonstrates the use of generators in Python"""


def inclusive_range(*args):
    """
    This functions is a generator similar to the built-in inclusive_range
    Args:
        *args: Minimum 1 and maximum 3 integer arguments for
        start, step, and stop
    Returns: A generator
    """
    numArgs = len(args)
    start = 0
    step = 1

    # Initiate Parameters
    if numArgs < 1:
        raise TypeError("expected at least 1 argument, got {}".format(numArgs))
    elif numArgs == 1:
        stop = args[0]
    elif numArgs == 2:
        (start, stop) = args
    elif numArgs == 3:
        (start, step, stop) = args
    else:
        raise TypeError("expected at most 3 arguments, got {}".format(numArgs))

    # generator
    i = start
    while i <= stop:
        yield i
        i += step


print range(25)
for i in inclusive_range(25):
    print i
