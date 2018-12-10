import os
import subprocess
import shlex
from datetime import datetime, timedelta
import time
from models import EMS_db_model
db = EMS_db_model()


def clock_in():
    print(db.record_attendance(2, 'clock-in', 'longview048'))
    print(db.record_attendance(3, 'clock-in', 'what the fuck'))


def clock_out():
    print(db.record_attendance(2, 'clock-out', 'longview048'))
    print(db.record_attendance(3, 'clock-out', 'what the fuck'))


for i in range(246):
    if i == 0:
        now = datetime.now()+ timedelta(days=1)

        date_str = now.strftime("%d %b %Y %H:%M:%S")

        subprocess.call(shlex.split("sudo date -s '%s'" % date_str))
        subprocess.call(shlex.split("sudo hwclock -w"))
        clock_in()
        print('first')
    else:
        if i % 2 == 0:

            yearint = int(datetime.now().year)

            monthint = int(datetime.now().month)

            dateint = int(datetime.now().day)

            now = datetime(yearint, monthint, dateint, 7, 00, 00, 00) + timedelta(days=1)

            date_str = now.strftime("%d %b %Y %H:%M:%S")

            subprocess.call(shlex.split("sudo date -s '%s'" % date_str))
            subprocess.call(shlex.split("sudo hwclock -w"))

            if i not in [21, 22, 45, 46, 57, 58, 89, 90, 91, 92, 101, 100]:
                clock_in()

            print('first')
        else:
            now = datetime.now() + timedelta(hours=8)

            date_str = now.strftime("%d %b %Y %H:%M:%S")

            subprocess.call(shlex.split("sudo date -s '%s'" % date_str))
            subprocess.call(shlex.split("sudo hwclock -w"))

            if i not in [21, 22, 45, 46, 57, 58, 89, 90, 91, 92, 101, 100]:
                clock_out()

            yearint = int(datetime.now().year)

            monthint = int(datetime.now().month)

            dateint = int(datetime.now().day)

            shift_datetime = datetime(yearint, monthint, dateint, 23, 58, 54, 00)

            shift_datetime_str = shift_datetime.strftime("%d %b %Y %H:%M:%S")
            subprocess.call(shlex.split("sudo date -s '%s'" % shift_datetime_str))
            subprocess.call(shlex.split("sudo hwclock -w"))

            time.sleep(10)
            print(datetime.now())
            subprocess.call(shlex.split("sudo date -s '%s'" % date_str))
            subprocess.call(shlex.split("sudo hwclock -w"))

            print('second')
