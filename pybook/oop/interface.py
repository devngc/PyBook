"""This module shows how a class can be used to as an interface."""

from abc import ABC, abstractmethod
from math import pi


class Planar_geometry(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_area(self):
        pass


class JSONify(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def to_json(self):
        pass


class Circle(Planar_geometry, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2
        
    def to_json(self):
        pass


cir = Circle(4)
print('Are of a circle with radius of {} is {}.'.format(cir.radius, round(cir.get_area(),
                                                                          2)))