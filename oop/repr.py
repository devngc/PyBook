"""This module shows the use of repr method that is used to customize the output of when
the class is printed."""


class Dog():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "I am a dirty {}".format(self.name)


tommy = Dog("Daas")
print(tommy)