"""This module demonstrates the customisation of magic methods"""


class SumList(object):

    def __init__(self, this_list):
        self.myList = this_list

    def __add__(self, other):
        newList = [x + y for x, y in zip(self.myList, other.myList)]
        return SumList(newList)

    def __repr__(self):
        return str(self.myList)


cc = SumList([1, 2, 3, 4, 5])
dd = SumList([100, 200, 300, 400, 500])

ee = cc + dd
print ee
