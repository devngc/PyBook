"""This script demonstrates the operations on collection objects"""

cars = ["bmw", "honda", "toyota"]
colors = ["red", "green", "blue", "yellow"]

for car, color in zip(cars, colors):
    print(car, "-->", color)
