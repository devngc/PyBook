"""This utility helps in sorting the zone wall names coming out of equest.
It groups the zone wall names alphabetically"""

import os
import csv


print ("current working directory is {}".format(os.getcwd()))
filePath = "W:\Dropbox\Github\PyBook\Rain Data"
print ("Now setting the current directory to the folder at {}".format(filePath))
os.chdir(filePath)
r = open("Present Weather Codes.csv", "r")

rain = []
squals = []

# Reading the file with zone names
if r.mode == "r":
    f1 = r.readlines()
    for x in f1:
        rain.append(int(x[1]))
        squals.append(int(x[2]))
r.close()


print len(rain)
print len(squals)

rainDataToWrite = [[item] for item in rain]
squalsDataToWrite = [[item] for item in squals]


# Writing to a new file
with open("rain.csv", "wb") as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(rainDataToWrite)
writeFile.close()

with open("squals.csv", "wb") as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(squalsDataToWrite)
writeFile.close()
