"""This script shows how to use the main function. Whenever a
python script is loaded, the script must be read fully before any
command is executed. The main function at The bottom of the script
helps in doing that."""

import platform


def main():
    message()


def message():
    print("This is python version {}".format(platform.python_version()))


if __name__ == '__main__':
    main()
