"""This module shows the use of enum. They are typically used to represent constant
values without duplication. """


from enum import Enum, unique, auto


# Duplicate values are allowed in the following class
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    TOMATO = 3
    ORANGE = 4
    PINEAPPLE = 1
    PEAR = auto()


print(" ")
print(Fruit.APPLE)
print(type(Fruit.APPLE))
print(repr(Fruit.APPLE))
print(Fruit.APPLE.name, Fruit.APPLE.value)
print('The automatically assigned value of Pear is {}'.format(Fruit.PEAR.value))
print(" ")

# Using enum as hash values
myFruits = {}
myFruits[Fruit.APPLE] = "Go bananas."

print(myFruits[Fruit.APPLE])
# You'll see that the value of APPLE remains 1
print(Fruit.APPLE.value)

# Duplicate values are not allowed
@unique
class Vegetables(Enum):
    POTATO = 1
    CUCUMBER = 1
