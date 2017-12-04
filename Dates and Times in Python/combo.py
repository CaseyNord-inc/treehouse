import datetime


# Write a function named time_tango that takes a date and a time. It should combine them into a datetime and return it.

def time_tango(date_arg, time_arg):
    return datetime.datetime.combine(date_arg, time_arg)
