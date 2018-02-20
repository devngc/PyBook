"""This module demonstrates the use of an abstract class"""
import abc


class getterSetter(object):
    """This is an abstract class. It cannot be instantiated."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, value):
        """Set a value in the instance"""
        return

    @abc.abstractmethod
    def get_val(self):
        """Get and return a value from the instance"""
        return


class Myclass(getterSetter):
    """Inheriting from the abstract class"""

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val


b = Myclass()
print b
