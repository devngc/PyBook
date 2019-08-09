"""This utility helps in sorting the zone wall names coming out of equest.
It groups the zone wall names alphabetically"""

import os
import csv


print "current working directory is {}".format(os.getcwd())
print "Now setting the current directory to the folder at {}".format(
    "C:\Users\devang.chauhan\Desktop\Python")
os.chdir("C:\Users\devang.chauhan\Desktop\Python")
r = open("zoneNames.csv", "r")

# Creating a list of alphabets
alphabet = []
for letter in range(65, 91):
    alphabet.append(chr(letter))

# Catching zone names in the next step
zoneNames = []

# Reading the file with zone names
if r.mode == "r":
    f1 = r.readlines()
    for x in f1:
        zoneNames.append(x.strip())
r.close()

# Creating a new list with zone names alphabetically arranged
master = []
for letter in alphabet:
    for name in zoneNames:
        if letter in name:
            master.append(name)


# List to write in a CSV file
dataToWrite = [[item] for item in master]

# Writing to a new file
with open("zoneNamesRevised.csv", "wb") as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(dataToWrite)

writeFile.close()
