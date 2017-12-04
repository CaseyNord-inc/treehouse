# Write a function named delorean that takes an integer. Return a datetime that is that many hours ahead from starter.

import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)


def delorean(integer):
    finisher = starter + datetime.timedelta(hours=integer)
    return finisher


# Write a function named time_machine that takes an integer and a string of "minutes", "hours", "days", or "years".
# This describes a timedelta. Return a datetime that is the timedelta's duration from the starter datetime.

# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.

## Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)


def time_machine(integer, string):
    if string == "minutes":
        finisher = starter + datetime.timedelta(minutes=integer)
    if string == "hours":
        finisher = starter + datetime.timedelta(hours=integer)
    if string == "days":
        finisher = starter + datetime.timedelta(days=integer)
    if string == "years":
        finisher = starter + datetime.timedelta(days=integer*365)
    return finisher
