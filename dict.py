"""This script demostrates some operations that can be done on
Python dictionaries"""
from itertools import izip
import json


# Printing dictionary with json module
map = {"a": 23, "b": 42, "c": "coffee"}
print json.dumps(map, indent=4, sort_keys=True), "\n"

# Creating disctionary from lists
cars = ["bmw", "honda", "toyota"]
colors = ["red", "green", "blue", "yellow"]
car_colors = dict(izip(cars, colors))
print "Creating a dictionary from lists"
print car_colors, "\n"

# Grouping with dictionaries
cars = ["bmw", "honda", "toyota", "mercedes", "subaru", "wolkswagen"]
d = {}
for car in cars:
    key = len(car)
    if key not in d:
        d[key] = []
    d[key].append(car)
print "Grouping with dictionary"
print d, "\n"

# Adding two dictionaries
capitals = {"USA": "Washington DC", "France": "Paris", "Italy": "Rome"}
more_Capitals = {"Germany": "Berlin", "Russia": "Moscow"}
capitals.update(more_Capitals)
print capitals, "\n"

# delete item
del capitals["USA"]

# Iterating over key and value both togather
print "Iterating over key and value pair togather"
for key, value in capitals.iteritems():
    print key, value
print "\n"

# Merging two dictionaries
x = {"name": "devang", "age": 29}
y = {"points": 25, "likes": ["science", "simulation"]}
z = dict(x, **y)
print z, "\n"

# Sort dictionary based on value
x = {"a": 1, "b": 2, "c": 3}
print sorted(x.items(), key=lambda x: x[1]), "\n"

# Using get() method on dictionaries with its default arguments
employees = {001: "Bob", 012: "Rob", 303: "John"}


def greetings(id):
    return "Hi {}!".format(employees.get(id, "there"))


for key in employees.keys():
    print greetings(key)
