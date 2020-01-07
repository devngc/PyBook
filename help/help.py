"""This module shows how to print help for the functions."""

import collections
import math
from math import *

# Print documentation for a class
print(collections.__doc__)

# Print documentation for the map function
print(map.__doc__)

# Printing all the methods in the math module
print(dir(math))

# printing the docstring of a function in the math module
print(sin.__doc__)

# See what a built in function does
print(help(len))