"""This script demonstrates the use of json module in Python"""

import json
import os


os.getcwd()
os.chdir("D:\Github\PyBook\json")

with open("sample.json") as fh:
    conf = json.load(fh)

print(conf)
print(type(conf))
