""" This document contains notes taken by MYA about datetime module """

import datetime


class Person(object):

    num_chromosomes = 46

    def __init__(self, name, surname, birthday):
        """ birthday is in form of (yyyy, mm, dd) but do not enter 01 use 1 """
        self.name = name.title()
        self.surname = surname.title()
        self.birthday = datetime.date(*birthday)

    def days_lived(self):
        """ date1 - date2 is a timedelta """
        tday = datetime.date.today()
        ret = tday - self.birthday
        return ret


tday = datetime.date.today()  # create today

print(tday)  # __str__ is applied
print(repr(tday))  # forced to apply __repr__

print(tday.weekday())  # Monday is 0
print(tday.isoweekday())  # Monday is 1

oneWeek = datetime.timedelta(days=7)
eightDays = datetime.timedelta(days=7, minutes=1440)
""" create 1 day and 1440 minutes of time duraiton """
print(tday + oneWeek)  # print today +7 days

yusuf = Person("yusuf", "aksel", (1998, 9, 10))

print("Name: {p.name}, Surname: {p.surname}, Birthday: {p.birthday}"
      .format(p=yusuf))

print(yusuf.days_lived())
print(yusuf.days_lived().days)
print(yusuf.days_lived().total_seconds())

# now pass to datetime.time

t = datetime.time(9, 30, 45, 100000)
print(t)

# now combine 'em all

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 1453)
print(dt)
print(dt.date())  # grab only date
print(dt.time())  # grab only time
print(dt.year)  # grab only one attribute

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)  # these two are same, the difference is due to exec. time
print(dt_utcnow)

""" continue from there : https://youtu.be/eirjjyP2qcQ?t=791 """
