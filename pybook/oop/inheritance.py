"""This script demonstrates inheritance with a simple example."""


class Animal(object):
    """This class is for animals"""
    def __init__(self, name):
        """This is the constructor"""
        self.name = name

    def eat(self, food):
        """This function is for eating food"""
        print('The {} is eating {}.'.format(self.name, food))


class Dog(Animal):
    """This is the dog class"""
    def fetch(self, thing):
        """This function prints the thing the dog chases"""
        print('The {} goes after {}.'.format(self.name, thing))


class Cat(Animal):
    """This class is for the cats"""
    def swatstring(self):
        print('{} shreds the string.'.format(self.name))


# Creating instances
theDog = Dog("Tommy")
theCat = Cat("Lucy")

# Caling instance methods
theDog.fetch("the shoe")
theCat.swatstring()

# Calling class method
theCat.eat("the dogshitt")
