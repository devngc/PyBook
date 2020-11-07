"""This script demonstrates the use of for loops in Python"""


def find(seq, tgt):
    for i, value in enumerate(seq):
        if value == tgt:
            break
    else:
        return -1
    return i


print find(range(11), 4)
