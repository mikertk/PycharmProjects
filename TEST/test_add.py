# coding=utf-8
import datetime
today = datetime.date.today()
numberDayAgo = today - datetime.timedelta(days=6)
print today
print numberDayAgo

time = 2016-04-06

if int(today) <= int(time) >= int(numberDayAgo):
    print "yes"
else:
    print ("no")
