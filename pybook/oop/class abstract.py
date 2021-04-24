"""This script demonstrates the use of an abstract class.
Here, Planar_geometry is an abstract class that cannot be instantiated. Also, the
instances of the this class must define a method named 'get_area'. """

from abc import ABC, abstractmethod
from math import pi


class Planar_geometry(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Planar_geometry):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.width * self.length


class Circle(Planar_geometry):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi*self.radius**2


rec = Rectangle(5, 6)
print('Area of a rectangle with width {} and length {} is {}.'.format(rec.width,
      rec.length, rec.get_area()))

cir = Circle(4)
print('Are of a circle with radius of {} is {}.'.format(cir.radius, round(cir.get_area(),
                                                                          2)))
