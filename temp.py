import datetime

tday = datetime.date.today()  # create today

print("Today:", tday)

""" create one week time duration """

oneWeek = datetime.timedelta(days=7)

""" create 1 day and 1440 minutes of time duraiton """

eightDays = datetime.timedelta(days=7, minutes=1440)

print("A week later than today:", tday + oneWeek)  # print today +7 days
