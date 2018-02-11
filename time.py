"""This file captures some methods to work with time in Python"""

from datetime import date
from datetime import time
from datetime import datetime


def main():

    # Dealing with dates
    today = date.today()
    print "Today's date is {}".format(today)
    print "Todays's date components are:\
    {}-{}-{}".format(today.day, today.month, today.year)
    print "Today's weekday # is: {}".format(today.weekday())
    days = ["Monday", "Tuesday", "Wednesday", "Thrsday",
            "Friday", "Saturday", "Sunday"]
    print "Which is a good {} \n".format(days[today.weekday()])

    # Dealing with Date-Time
    now = datetime.now()
    print now.strftime("It is %dth %b of %y, and a %a")
    print now.strftime("It is %dth %B of %Y, and a %A \n")

    # Dealing with Locale's time style
    print now.strftime("Locale's date and time: %c")
    print now.strftime("Locale's date: %x")
    print now.strftime("Locale's time: %X \n")


if __name__ == '__main__':
    main()
