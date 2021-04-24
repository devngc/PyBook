#!/usr/bin/python3

"""This module shows how key word arguments can be provided in the class
constructor."""


class Animal:
    def __init__(self, **kwargs):
        # The following are all class attributes
        self.type = kwargs['type'] if 'type' in kwargs else 'Dog'
        self.name = kwargs['name'] if 'name' in kwargs else 'Tommy'
        self.sound = kwargs['sound'] if 'sound' in kwargs else 'Whow whow'

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def get_sound(self):
        return self.sound


amir = Animal()
print(amir.get_type())
