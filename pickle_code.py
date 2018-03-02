import pickle

myList = ["a", "b", "c", "d"]

# with open("datafile.txt", "w") as fh:
#     pickle.dump(myList, fh)

with open("datafile.txt", "r") as fh:
    unpackedList = pickle.load(fh)

print unpackedList, "\n"

# X stores the python object as a string.
# This is done when you don't with to write to a file
x = pickle.dumps(["a", "b", 1, 2.3])
var = pickle.loads(x)
print var
print x
