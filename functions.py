"""This file captures the interesting and \
useful things I found out about the functions in Python"""


def main():
    optionalArgsFunc(1, 2, 3, 4, 5, 6)
    namedFunc(1, 2, 3,4,5,6, extra = 11, next = 22, lost = 35)


def optionalArgsFunc(this, that, *args):
    """Function demonstrating the use of optional arguments"""
    print this, that, " and the other optional arguments are ", args


def namedFunc(this, that, other, *args, **kwrgs):
    print "This function outputs {} {} {}and{}\
    and also {}".format(this, that, other, args, kwrgs)


if __name__ == "__main__":
    main()
