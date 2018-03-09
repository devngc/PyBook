"""This file is frequently used to try new things. Contents change
almost on a daily basis."""

def threeMultis(lst):
    if isinstance(lst, list):
        resultList = [item for item in lst if item % 3 == 0 and item != 0]
        return resultList
    else:
        return "List input of numbers required"


print ("This is a really long string."
       " Just trying this out right now."
       " As per the latest book that I am reading"
       " called 'Python-tricks'.")
