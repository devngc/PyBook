"""This file is used to perform file modifications in thid directory"""

import os


def rename(old, new):
    """Renaming a file"""
    try:
        os.rename(old, new)
        print "File successfully renamed"
    except Exception as e:
        print e


def remove(extension):
    """Removing files of specific extension"""
    dirs = os.listdir(os.getcwd())
    for file in dirs:
        if extension in file:
            print "{} will be removed". format(file)
            os.remove(file)


remove(".pyc")
