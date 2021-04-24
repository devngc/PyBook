"""This script demostrates exception handling in Python"""

import sys

myDict = {"a": 1, "b": 2, "c": 3, "d": 4}
key = raw_input("Please input a key: ")

try:
    print "Testing for error"
    print "The value for {} is {}".format(key, myDict[key])
except KeyError:
    print "Trapped error"
    print "The key " + key + " does not exist"
    sys.exit()


try:
    arg = sys.argv[1]   # This accepts argument on the command line
    num = int(arg)
except (IndexError, ValueError):
    exit("Please enter an integer on the command line")

print "Thanks for the integer iput"


def make_delim_line(list_to_join, delim):
    try:
        formatted_line = delim.join(list_to_join)
    except TypeError:
        raise TypeError("make_delim_line(): arg 1 must be a list or tuple")
    return formatted_line


fline = make_delim_line(100, ",")
