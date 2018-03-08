def threeMultis(lst):
    if isinstance(lst, list):
        resultList = [item for item in lst if item % 3 == 0 and item != 0]
        return resultList
    else:
        return "List input of numbers required"

print "HI"
