"""This module demonstrates the use of string representations."""


class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return "It is a {} car with mileage of {}".format(self.color, self.mileage)

    def __repr__(self):
        return "A {} car".format(self.color)

    def __bytes__(self):
        val = 'It is a {} car with the mileage of {}.'.format(self.color, self.mileage)
        return bytes(val.encode('utf-8'))


my_car = Car("red", 132)


print(repr(my_car))
print(str(my_car))
print('Formatted class is {}'.format(my_car))
print(bytes(my_car))