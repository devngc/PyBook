"""This file captures the interesting and
useful things I found out about the functions in Python"""


def main():
    optionalArgsFunc(1, 2, 3, 4, 5, 6)
    namedFunc(1, 2, 3, 4, 5, 6, extra=11, next=22, lost=35)
    defaultValue()


def optionalArgsFunc(this, that, *args):
    """Function demonstrating the use of optional arguments"""
    print(this, that, " and the other optional arguments are ", args)


def namedFunc(this, that, other, *args, **kwrgs):
    """This function prints the regaular arguments,
    the extra arguments, and the keyword arguments"""
    print(("This function outputs {} {} {} " + "then {} and also {}"
           ).format(this, that, other, args, kwrgs))


def defaultValue(n=1):
    """This function simply prints the default argument given
    to the function."""
    print(n)


if __name__ == "__main__":
    main()
