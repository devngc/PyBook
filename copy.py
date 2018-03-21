"""This script shows the use of os copy method in Shutil module"""


import shutil
import os
os.chdir("G:\Dropbox\Github\PyBook")

if os.path.exists("sample.txt"):

    src = os.path.realpath("sample.txt")
    dst = src + ".bak"

    # Normal copy and copy with metadata
    shutil.copy(src, dst)
    shutil.copystat(src, dst)

else:
    print "File not found"
