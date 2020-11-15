"""This script shows a very basic class in python."""


class Dog:
    """This is a dog class.
    The functions in this class are
    called the methods of the dog class.
    The variables in the class are called
    the class variables"""

    def bark(self):
        print("Whow Whow")

    def walk(self):
        print("I don't like to walk")

    height = 1.5


def main():
    scooby = Dog()
    scooby.bark()
    scooby.walk()
    print(scooby.height)


if __name__ == '__main__':
    main()
