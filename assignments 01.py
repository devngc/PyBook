"""This module is the first assignment in the Python BB"""


class MaxSizeList(object):
    """
    This class takes an integer as an argument. \
    This value will be used \
    to return the number \
    of item of the list that \
    will be returned
    """
    def __init__(self, size):
        self.max_size = size
        self.list = []

    def push(self, item):
        """Adds the item to the list initiated with the instance."""
        self.list.append(item)

    def get_list(self):
        """Return the list with the items counted from the end of \
        the list. The number of items is equal to the max_size"""
        if isinstance(self.max_size, int) and self.max_size > 0:
            output = self.list[(self.max_size)*-1:]
        else:
            output = "The value for size has to be an integer please"
        return output
