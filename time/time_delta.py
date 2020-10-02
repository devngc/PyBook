"""This file captures some methods to work with time delta in Python"""

from datetime import date
from datetime import datetime
from datetime import timedelta


def main():
    # Testing time delta
    print timedelta(days=365, hours=5, minutes=1)

    # One year from now
    now = datetime.now()
    print "One year from now it will be: " + str(now + timedelta(days=365))

    # In a near future
    print "In 2 days and 3 weeks it will be: " + str(
        now + timedelta(days=2, weeks=3))

    # In the immediate past
    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print "One week ago it was: " + s

    # Time from the April fool's day
    today = date.today()
    afd = date(today.year, 4, 1)
    if afd < today:
        print "April fool's day has already \
        passed {} days ago".format((today-afd).day)
        afd = afd.replace(year=today.year+1)
    timeToAfd = afd - today
    print "It's just {} days untill the next \
        April fool's day.".format(timeToAfd)


if __name__ == '__main__':
    main()
