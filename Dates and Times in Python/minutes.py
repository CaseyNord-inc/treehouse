def minutes(dtime1, dtime2):
    deltat = dtime2 - dtime1
    return round(deltat.total_seconds() / 60)
