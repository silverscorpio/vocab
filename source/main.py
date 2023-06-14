import datetime
from datetime import timedelta

t0 = datetime.datetime.today()
while True:
    t0 += timedelta(seconds=1)
    print(t0.strftime("%H:%M:%S"))
