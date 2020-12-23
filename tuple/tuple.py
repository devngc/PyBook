"""This script demonstrates the use of named tuple
from the collection module"""

from collections import namedtuple

# Creating a class using the namedtuple method
Car = namedtuple('Car', 'color mileage type')
my_car = Car('red', 3812.4, "sedan")
print(my_car.color)
print(my_car.mileage)
print(my_car.type)
print(my_car)
print(my_car.color)
black_car = my_car._replace(color="Black")
print(black_car)