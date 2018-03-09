"""This module demonstrates how the
__init__ constructor in the parent class can
be inherited in the instance class."""

import random


class Animal(object):
    """This is the animal class"""

    def __init__(self, name):
        self.name = name


class Dog(Animal):
    """This is the dog class"""

    def __init__(self, name):
        # The next statement is very important here
        # We could also write Animal.__init__(name)
        # This would create trouble for us if the
        # parent class were to change in the future
        super(Dog, self).__init__(name)
        self.breed = random.choice(["shin Tzu", "Beagle", "Mutt"])

    def fetch(self, thing):
        print "%s goes after the %s" % (self.name, thing)


d = Dog("peter")

print d.name
print d.breed
