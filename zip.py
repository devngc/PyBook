"""This script shows the use of os zipFile method in zipfile module"""

from zipfile import ZipFile
import os
os.chdir("G:\Dropbox\Github\PyBook")

try:
    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("sample.txt")
        newzip.write("sample.txt.bak")

except Exception as e:
    print e.message
