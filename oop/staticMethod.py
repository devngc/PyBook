"""This script demonstrates the use of Static Method"""


class InstanceCounter(object):
    """This class is similar to the InstanceCounter class \
    Here, a use of the static method is demonstrated """
    count = 0

    def __init__(self, val):
        self.val = self.filterVal(val)
        InstanceCounter.count += 1

    @staticmethod
    def filterVal(value):
        if not isinstance(value, int):
            return 0
        else:
            return value


a = InstanceCounter(5)
b = InstanceCounter("Hello")
c = InstanceCounter(13)
d = InstanceCounter(17)

print a.val
print b.val
print c.val
print d.val
