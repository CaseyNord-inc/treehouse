# Create a variable named moscow that holds a datetime.timezone object at +4 hours.

import datetime

moscow = datetime.timezone(datetime.timedelta(hours=4))
pacific = datetime.timezone(datetime.timedelta(hours=-8))
india = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
