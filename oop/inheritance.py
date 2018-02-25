"""This script demonstrates inheritence with a simple exameple"""


class Animal(object):
    """This class is for animals"""
    def __init__(self, name):
        """This is the constructor"""
        self.name = name

    def eat(self, food):
        """This function is for eating food"""
        print "%s is eating %s" % (self.name, food)


class Dog(Animal):
    """This is the dog class"""
    def fetch(self, thing):
        """This function prints the thing the dog chases"""
        print "%s goes after %s" % (self.name, thing)


class Cat(Animal):
    """This class is for the cats"""
    def swatstring(self):
        print "%s shreds the string" % (self.name)


# Creating instanses
theDog = Dog("Tommy")
theCat = Cat("Lucy")

# Caling instance methods
theDog.fetch("the shoe")
theCat.swatstring()

# Calling class method
theCat.eat("the dogshitt")
