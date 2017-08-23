from datetime import datetime

import pytz

OTHER_TIMEZONES = [
    pytz.timezone('US/Pacific'),
    pytz.timezone('Japan'),
    pytz.timezone('Singapore'),
    pytz.timezone('Pacific/Honolulu'),
    pytz.timezone('Libya'),
    pytz.timezone('Iceland'),
    pytz.timezone('Poland'),
    pytz.timezone('UTC')
]

fmt = '%m-%d %H:%M:%S %Z%z'

while True:
    date_input = input("When is your meeting? Please use MM/DD/YYYY HH:MM format. ")
    try:
        local_date = datetime.strptime(date_input, '%m/%d/%Y %H:%M')
    except ValueError:
        print("{} doesn't seem to be a valid date & time.".format(date_input))
    else:
        local_date = pytz.timezone('US/Pacific').localize(local_date)
        utc_date = local_date.astimezone(pytz.utc)

        output = []
        for timezone in OTHER_TIMEZONES:
            output.append(utc_date.astimezone(timezone))
        for appointment in output:
            print(appointment.strftime(fmt))
        break
