"""This script demostrates exception handling in Python"""
import sys


# Example 01
def main():
    try:
        x = 5/0
    except ValueError:
        print("A value error is caught")
    except:
        print("Unknown error is " + str(sys.exc_info()[1]))
    else:
        print("it worked fine")


if __name__ == '__main__':
    main()
