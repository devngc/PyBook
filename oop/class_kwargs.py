#!/usr/bin/python3

"""This module shows how key word arguments can be provided in the class
constructor."""


class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'Dog'
        self._name = kwargs['name'] if 'name' in kwargs else 'Tommy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'Whow whow'

    def get_type(self):
        return self._type

    def get_name(self):
        return self._name

    def get_sound(self):
        return self._sound


amir = Animal()
print(amir.get_type())
