from contextlib import contextmanager
import os
os.chdir("G:\Dropbox\Github\PyBook")


@contextmanager
def managed_file(name):
    try:
        f = open(name, "w")
        yield f
    finally:
        f.close()


with managed_file("sample.txt") as f:
    f.write("Start of the demo of contextmanager")
    f.write("End of the demo of the contextmanager")
