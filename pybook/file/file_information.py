"""This script demostrates file operations through Python"""

import os
from os import path
import datetime
import time


def main():
    print(os.name)
    print("Item exists: " + str(path.exists("sample.txt")))
    print("Item is a file: " + str(path.isfile("sample.txt")))
    print("Item is a directory: " + str(path.isdir("sample.txt")))

    # Full path
    print("Item path: " + str(path.realpath("sample.txt")))
    print("Item path and name: " + str(path.split(path.realpath("sample.txt"))))

    # Modification Time
    t = time.ctime(path.getmtime("sample.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("sample.txt")))

    # How long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(
        path.getmtime("sample.txt"))
    print("It has been {} or {} seconds"
          " since the file was modified ".format(td, td.total_seconds()))


if __name__ == "__main__":
    main()
