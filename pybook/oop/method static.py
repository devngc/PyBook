"""This script demonstrates the use of Static Method"""


class InstanceCounter(object):

    count = 0

    def __init__(self, val):
        self.val = self.filterVal(val)
        InstanceCounter.count += 1

    # A static method is really more like a helper method
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

print(a.val, InstanceCounter.count)
print(b.val, InstanceCounter.count)
print(c.val, InstanceCounter.count)
print(d.val, InstanceCounter.count)
