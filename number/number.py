"""This module shows how to deal with scientific noations in numbers."""
from decimal import *

a = .1 + .1 + .1 - .3
print(a)

b = Decimal('.10')
c = Decimal('.30')
d = b + b + b - c
print(d)
