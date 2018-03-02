import os

variables = os.getenv("PATH").split(";")
for item in variables:
    print item
