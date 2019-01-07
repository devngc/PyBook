"""This script demonstrates the use of __str__ methods"""


class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return "It is a {} car with mileage of {}".format(
            self.color, self.mileage)

    def __repr__(self):
        return "A {} car".format(self.color)


my_car = Car("red", 132)
my_car
