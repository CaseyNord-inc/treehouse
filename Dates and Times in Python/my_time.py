import datetime
import pytz

fmt = '%m-%d %H:%M %Z%z'
my_time = datetime.datetime.now()

pacific = pytz.timezone('US/Pacific')
japan = pytz.timezone('Japan')
singapore = pytz.timezone('Singapore')
hawaii = pytz.timezone('Pacific/Honolulu')
libya = pytz.timezone('Libya')
iceland = pytz.timezone('Iceland')
poland = pytz.timezone('Poland')

local = pacific.localize(my_time)
print(my_time.strftime(fmt))
timezones = [pacific, japan, singapore, hawaii, libya, iceland, poland]
for time in timezones:
    print(my_time.astimezone(time).strftime(fmt))
