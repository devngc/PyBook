"""This module constains some inheritance examples"""
import abc


class GetSetParent(object):
    """This is the abstract class that can not be instantiated"""
    __metaclass__ = abc.ABCMeta

    def __init__(self, value):
        self.val = 0

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        return


class GetSetInt(GetSetParent):
    """This class inherits from the abstract class GetSetParent"""

    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_val(value)

    def showdoc(self):
        print "GetSetInt object ({0}), only accepts "\
            "integer values. " .format(id(self))


class GetSetList(GetSetParent):
    """This class inherits from the abstract class GetSetParent"""

    def __init__(self, value=0):
        self.vallist = [value]

    def get_val(self):
        return self.vallist[-1]

    def get_vals(self):
        return self.vallist

    def set_val(self, value):
        self.vallist.append(value)

    def showdoc(self):
        print "GetSetList object, len {0}, stores "\
            "history of values set".format(len(self.vallist))


gsl = GetSetList(5)
gsl.set_val(10)
gsl.set_val(20)
print gsl.get_val()
print gsl.get_vals()
gsl.showdoc()
