"""This script demonstrates MRO in OOP"""

# This is an example of tree shaped inheritance pattern


class A(object):
    """Class A"""
    def doTHis(self):
        print "Doing this inside A"


class B(A):
    """Class B the child of class A"""
    pass


class C(object):
    """Class C"""
    def doThis(self):
        print "Doing this inside C"


class D(B, C):
    """Class D inherits from class B and class C"""
    pass


d_instance = D()
d_instance.doTHis()

# Following is the most important attribute call in this script.
# Study the output of this call carefully
# It display how python is looking up for an attribute
# This is called MRO, or Method Resolution Order

print D.mro()


# Now let's look at the dimond shape inheritance pattern


class A(object):
    """Class A"""
    def doTHis(self):
        print "Doing this inside A"


class B(A):
    """Class B the child of class A"""
    pass


class C(A):
    """Class C the child of class A"""
    def doThis(self):
        print "Doing this inside C"


class D(B, C):
    """Class D inherits from class B and class C"""
    pass


d_instance = D()
d_instance.doTHis()
print D.mro()
