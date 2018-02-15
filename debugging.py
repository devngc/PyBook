"""This script demonstraes the use of Python Debugging Package.
It requires the PDP package to be installed"""

import pdp

values = range(1, 11)
for val in values:
    mysum = 0
    mysum += val
    pdp.set_trace()
print mysum
