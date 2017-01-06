# coding=utf-8
import datetime


def TimeArea(number):
    today = datetime.date.today()
    numberDayAgo = today - datetime.timedelta(days=number)
    print today
    print numberDayAgo


TimeArea(2)


# time = 2016-04-06
#
# if today < = time

def sleep(param):
    return None
