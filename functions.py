"""This file captures the interesting and \
useful things I found out about the functions in Python"""


def main():
    optionalArgsFunc(1, 2, 3, 4, 5, 6)


def optionalArgsFunc(this, that, *args):
    """Function demonstrating the use of optional arguments"""
    print this, that, " and the other optional arguments are ", args


if __name__ == "__main__":
    main()
