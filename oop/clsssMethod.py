"""This script demonstrates the use of class method and static method"""


class InstanceCounter(object):
    """This class counts the number of times the class is instantiated"""
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    # def get_count(self):
    #     return InstanceCounter.count

    # The instance method above is turned into a class method below
    # CLS is the class instance
    @classmethod
    def get_count(cls):
        return cls.count


a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
    print "val of obj: %s" % (obj.get_val())
    print "count: %s" % (obj.get_count())
