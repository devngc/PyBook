"""This script demonstrates the use of class method and static method"""


class InstanceCounter:
    """This class counts the number of times the class is instantiated"""

    __count = 0  # Class variable
    # A class variable is available to all the instances of a class

    def __init__(self, val):
        self.val = val
        InstanceCounter.__count += 1

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    # def get_count(self):
    #     return InstanceCounter.__count

    # The instance method above is turned into a class method below
    # CLS is the class instance
    @classmethod
    def get_count(cls):
        """This methods returns the number of times a class is instantiated."""
        return cls.__count


a = InstanceCounter(5)
a.set_val(25)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
    print(obj.get_val(), obj.get_count(), InstanceCounter.get_count())
