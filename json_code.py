"""This script demonstrates the use of json module in Python"""

import json

with open("sample.json") as fh:
    conf = json.load(fh)

print(conf)
print(type(conf))
