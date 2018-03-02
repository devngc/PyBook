"""This file is used to perform file modifications in thid directory"""

import os

# Renaming a file
try:
    os.rename("unitTest.py", "myprogram.py")
    print "File successfully renamed"
except Exception as e:
    print e

# Removing compiled files
dirs = os.listdir(os.getcwd())
for file in dirs:
    if ".pyc" in file:
        print "{} will be removed". format(file)
        os.remove(file)
