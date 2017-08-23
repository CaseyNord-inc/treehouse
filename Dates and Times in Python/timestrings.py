import datetime

## Examples
# to_string(datetime_object) => "24 September 2012"
# from_string("09/24/12 18:30", "%m/%d/%y %H:%M") => datetime


def to_string(datetime_object):
    return datetime.datetime.strftime(datetime_object, '%d %B %Y')


to_string("24 January 2016")
