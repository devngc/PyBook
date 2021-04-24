"""This script demonstrated polymorphism with a simple example.
Please pay attention to the show_affection method that is defined
in both the classes"""


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

    def show_affection(self):
        """This function shows affection to the dog"""
        print "{0} wags tail".format(self.name)


class Cat(Animal):
    """This class is for the cats"""
    def swatstring(self):
        print "%s shreds the string" % (self.name)

    def show_affection(self):
        """This function shows affection to the cat"""
        print "{0} purrs".format(self.name)


# Creating instanses
theDog = Dog("Tommy")
theCat = Cat("Lucy")

# Caling instance methods
theDog.fetch("the shoe")
theCat.swatstring()

# Calling class method
theCat.eat("the dogshitt")

# Showing affection
for a in (Dog("Rover"), Cat("Fluffy"), Cat("Precious"), Dog("Scout")):
    a.show_affection()
