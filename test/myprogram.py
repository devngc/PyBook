"""The file is to be used for testing from the test_myprogram.py"""
import sys


def doubleit(x):
    if not isinstance(x, (int, float)):
        raise TypeError
    var = x * 2
    return var


if __name__ == "__main__":
    input_val = sys.argv[1]
    double_val = doubleit(input_val)
    print "The value of {} is {}".format(input_val, double_val)
