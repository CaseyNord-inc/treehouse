# Create a function named timestamp_oldest that takes any number of POSIX timestamp arguments. Return the oldest one as a datetime object.

# Remember, POSIX timestamps are floats and lists have a .sort() method.

# If you need help, look up datetime.datetime.fromtimestamp()
# Also, remember that you *will not* know how many timestamps
# are coming in.

import datetime


def timestamp_oldest(*args):
    return datetime.datetime.fromtimestamp(min(args))
