"""This script demostrates file operations through Python"""

import os
from os import path
import datetime
import time


def main():
    print os.name
    print "Item exists: " + str(path.exists("text.txt"))
    print "Item is a file: " + str(path.isfile("text.txt"))
    print "Item is a directory: " + str(path.isdir("text.txt"))

    # Full path
    print "Item path: " + str(path.realpath("text.txt"))
    print "Item path and name: " + str(path.split(path.realpath("text.txt")))

    # Modification Time
    t = time.ctime(path.getmtime("text.txt"))
    print t
    print datetime.datetime.fromtimestamp(path.getmtime("text.txt"))

    # How long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(
        path.getmtime("text.txt"))
    print "It has been {} or {} seconds \
    since the file was modified ".format(td, td.total_seconds())


if __name__ == "__main__":
    main()
