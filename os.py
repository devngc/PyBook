"""This script shows the use of os module"""

import os


print "current working directory is {}".format(os.getcwd())
print "Now setting the current directory to the Pybook folder at {}".format(
    "G:\Dropbox\Github\PyBook")
os.chdir("G:\Dropbox\Github\PyBook")

# Rename file
os.rename("sample.txt", "newSampleFile.txt")
