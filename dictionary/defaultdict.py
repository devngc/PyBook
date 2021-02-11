"""This module shows the use of default dict. Here, default dict is used to assign
default values for the keys that exist. Here, that value will be an integer."""

from collections import defaultdict

names = ['ramesh', 'rakesh', 'suresh', 'champesh', 'murkhesh', 'ramesh']

roll_numbers = defaultdict(int)

for name in names:
    roll_numbers[name] += 1

for key, value in roll_numbers.items():
    print(key, value) 