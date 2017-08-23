# naive is a datetime with no timezone.
# Create a new timezone for US/Pacific, which is 8 hours behind UTC (UTC-08:00).
# Then make a new variable named hill_valley that is naive with its tzinfo attribute replaced with the US/Pacific timezone you made.

import datetime

naive = datetime.datetime(2015, 10, 21, 4, 29)

pacific = datetime.timezone(datetime.timedelta(hours=-8))

hill_valley = datetime.datetime(2015, 10, 21, 4, 29, tzinfo=pacific)

# Great, but replace just sets the timezone, it doesn't move the datetime to the new timezone. Let's move one.
# Make a new timezone that is UTC+01:00.
# Create a new variable named paris that uses your new timezone and the astimezone method to change hill_valley to the new timezone.

new_timezone = datetime.timezone(datetime.timedelta(hours=1))

paris = hill_valley.astimezone(new_timezone)
