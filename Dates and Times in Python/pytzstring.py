# starter is a naive datetime. Use pytz to make it a "US/Pacific" datetime instead and assign this converted datetime to the variable local.

import datetime
import pytz

fmt = '%m-%d %H:%M %Z%z'
starter = datetime.datetime(2015, 10, 21, 4, 29)
pacific = pytz.timezone('US/Pacific')
local = pacific.localize(starter)

# Now create a variable named pytz_string by using strftime with the local datetime. Use the fmt string for the formatting.

pytz_string = local.astimezone(pacific).strftime(fmt)
