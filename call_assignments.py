"""This module imports the assignments and checks them"""

from assignments import MaxSizeList

# Calling assignment 01
A = MaxSizeList(2)
A.push("gog")
A.push("dog")
A.push("hog")
print A.get_list()
