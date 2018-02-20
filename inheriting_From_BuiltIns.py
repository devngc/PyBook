"""This module demonstrates how you inherit from Python built-in classes"""


class MyDict(dict):
    pass


dd = MyDict()
dd["a"] = 5
dd["b"] = 6

for key in dd.keys():
    print "{0} = {1}".format(key, dd[key])
