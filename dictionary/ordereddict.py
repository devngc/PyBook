"""This module shows the use if ordered dict."""

from collections import OrderedDict

first = OrderedDict({'a': 0, 'b': 1, 'c': 3, 'd': 4})
second = OrderedDict({'a': 0, 'b': 1, 'd': 4, 'c': 3})
third = {'a': 0, 'b': 1, 'd': 4, 'c': 3} # Copy of second but not an Ordereddict
print('Equality test: {}'.format(first == second))
print('Equality test: {}'.format(first == third))