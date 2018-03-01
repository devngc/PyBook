# Module names: all_lower_case
# Globals and locals: all_lower_case
# Functions and methods: all_lower_case
# Class names and exception names: CamelCase
# Constants: ALL_CAPS

# Public attributes or variabels intended to be used by the
# importer of this module or user of this class: regular_lower_case

# Private attributes or variables fr internal use by the
# module or class: _signle_leading_underscore

# Private attributes that shouldn't be subclassed: __double_leading_underscore

# Magic attributes: __double_underscores__


class GetSet(object):

    instance_count = 0

    # Following is a special variable
    # It is not intended to be subclassed
    __mangled_name = "no privacy"

    def __init__(self, value):
        self._attrval = value
        GetSet.instance_count += 1

    @property
    def var(self):
        print "Getting the 'var' attribute"
        return self._attrval

    @var.setter
    def var(self, value):
        print "Setting the 'var' attribute"
        self._attrval = value

    @var.deleter
    def var(self):
        print "Deletig the 'var' attribute"
        self._attrval = None


cc = GetSet(5)
cc.var = 10
print cc._attrval
# Comment out this line below and see what happens
# Having double underscores in a variable name does infuse some privacy
# print cc.__mangled_name
# The mangled name attribute has to be called with this special way
print cc._GetSet__mangled_name
