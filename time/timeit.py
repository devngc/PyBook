"""This file captures some methods to work with timeit module in Python"""

import timeit

print "by index: ", timeit.timeit(
    stmt="mydict['c']",
    setup="mydict = {'a':5, 'b': 6, 'c':7}",
    number=1000000)
print "by get: ", timeit.timeit(
    stmt="mydict['c']",
    setup="mydict = {'a':5, 'b': 6, 'c':7}",
    number=1000000)
