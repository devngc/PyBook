"""This script demonstrates the operations on collection objects"""

from itertools import izip

cars = ["bmw", "honda", "toyota"]
colors = ["red", "green", "blue", "yellow"]

for car, color in izip(cars, colors):
    print car, "-->", color
