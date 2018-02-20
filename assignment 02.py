"""This module is the solution for assignment 02 in Python BB"""

import abc
import datetime


class WriteFile(object):
    """This is an abstract class that can't be instantiated and write files"""
    __metaclass__ = abc.ABCMeta
    # Following is the absolute path where files shall be created
    path = "D:\Dropbox\Github\Work-in-Progress\PythonBB\\"

    @abc.abstractmethod
    def write(self, content, fileName, delimiter=None):

        if isinstance(content, str) and delimiter is None:
            dt_str = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
            content = dt_str + " " + content
            fileName = WriteFile.path + fileName
            file = open(fileName, "a")
            file.write(content)
            file.write("\n")
            file.close()

        if isinstance(content, list) and delimiter is not None:
            fileName = WriteFile.path + fileName
            file = open(fileName, "a")
            for i in range(len(content)-1):
                add = str(content[i]) + delimiter
                file.write(add)
            file.write(str(content[-1]))
            file.write("\n")
            file.close()


class LogFile(WriteFile):
    """This class inherits from the WriteFile class"""
    def __init__(self, fileName):
        self.fileName = fileName

    def write(self, content):
        super(LogFile, self).write(content, self.fileName)


class DelimFile(WriteFile):
    """This class inherits from the WriteFile class"""
    def __init__(self, fileName):
        self.fileName = fileName

    def write(self, content, delimiter):
        super(DelimFile, self).write(content, self.fileName, delimiter)


log = LogFile("log.txt")
myDelim = DelimFile("data.csv")

log.write("this is a log message")
log.write("this is another log message")

myDelim.write(["a", "b", "c", "d"], ",")
myDelim.write([1, 2, 3, 4], ";")
