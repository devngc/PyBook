#!/usr/bin/python3

"""This script shows a very basic class in python."""


class Dog:
    """This is a dog class.
    The functions in this class are
    called the methods of the dog class.
    The variables in the class are called
    the class variables """
    # The following two are class variables and are availale to all the instances
    sound = "Whow Whow"
    swag = "i don't like to walk"

    def bark(self):
        print(self.sound)

    def walk(self):
        print(self.swag)

def main():
    scooby = Dog()
    scooby.bark()
    scooby.walk()
    # While the following is not a good practice, it is allowed
    print(scooby.sound)
    print(scooby)


if __name__ == '__main__':
    main()
