try:
    with open("text.txt") as fh:
        for line in fh:
            line = line.rstrip()
            print line
    # After the with block is executed, Python closes the file
except Exception, e:
    print e
finally:
    print "done! \n"


class MyClass(object):

    def __enter__(self):
        print "We have entered the 'with' block"
        return self

    def __exit__(self, type, value, traceback):
        print "We're leaving the 'with'"

    def sayHi(self):
        print "Hi, instance %s" % (id(self))


with MyClass() as cc:
    cc.sayHi()

print "After the with block"
