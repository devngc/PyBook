

def main():
    # Writing to a file
    f = open("text.txt", "w+")
    for i in range(10):
        f.write("This is line number {} \r\n".format(i))
    f.close()

    # Appending to a file
    f = open("text.txt", "a")
    for i in range(10):
        f.write("This is line number {} \r\n".format(i))
    f.close()

    # Reading a file
    r = open("text.txt", "r")
    if r.mode == "r":
        contents = r.read()
        print contents
    r.close()

    # Reading line by line
    r = open("text.txt", "r")
    if r.mode == "r":
        fl = r.readlines()
        for x in fl:
            print x, "This is one line"
    r.close()


if __name__ == "__main__":
    main()
