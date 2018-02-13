"""This file demonstrates the use of calendars in python"""

import calendar
c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2017, 1, 0, 0)
print st

# HTML calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2017, 1)
print st

# Dates of the month
for i in c.itermonthdays(2017, 8):
    print i

# Months in a year as per Locale
for name in calendar.month_name:
    print name

# # Days in a week as per Locale
for day in calendar.day_name:
    print day

# Priting a particualr date on each month
print "Team meetings will be on: "
for m in range(1, 13):
    cal = calendar.monthcalendar(208, m)
    weekOne = cal[0]
    weekTwo = cal[1]

    if weekOne[calendar.FRIDAY] != 0:
        meetday = weekOne[calendar.FRIDAY]
    else:
        meetday = weekTwo[calendar.FRIDAY]

    print "%10s %2d" % (calendar.month_name[m], meetday)
