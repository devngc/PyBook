import os
from os import path
import shutil
from zipfile import ZipFile


def main():
    if path.exists("text.txt"):

        src = path.realpath("text.txt")
        dst = src + ".bak"

        # Normal copy and copy with metadata
        shutil.copy(src, dst)
        shutil.copystat(src, dst)

        # Rename file
        os.rename("text.txt", "newFile.txt")

        # Make archive
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir=root_dir)

        # Make archive with specific files
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("text.txt")
            newzip.write("text.txt.bak")


if __name__ == "__main__":
    main()
