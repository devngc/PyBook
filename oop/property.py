"""This script demonstrates the proprty operator"""


class GetSet(object):

    def __init__(self, value):
        self.attrval = value

    @property
    def var(self):
        print "getting the var attribute"
        return self.attrval

    @var.setter
    def var(self, value):
        print "Setting the 'var' attribute"
        self.attrval = value

    @var.deleter
    def var(self):
        print "deleting the 'var' attribute"
        self.attrval = None


me = GetSet(5)
me.var = 1000
print me.var
del me.var
print me.var
