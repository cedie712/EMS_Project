from models import EMS_db_model
import json
from datetime import date, datetime
import calendar
from face import Identifier, dataSetCreator
db = EMS_db_model()
import requests
from threading import Timer
import time
import signal
import schedule
import time
from datetime import timedelta
from pytz import timezone
from itertools import groupby


# test cases
def register():
    content = {
        'username': 'cooldude',
        'password': 'longview048',
        'confirm': 'longview048',
        'email': 'cedrick044',
        'fname': 'jolo',
        'mname': 'cuizon',
        'lname': 'domingo',
        'position': 'instructor',
        'is_admin': False,
        "sss_number": "3242-2342342-4234",
        "pagibig_number": "3242-4234-2342",
        "philhealth_number": "23-423423423-2",
        "tin_number": "324-432-423-23423",
        'rate': 100.0,
        'day_off': 'tuesday',
        'birthday': '2000-04-08',
        'address': 'gapan',
        'gender': 'male',
        'height': 143,
        'contact_number': '9951079021',
    }

    x = db.register_user(content)
    return x

# registerUser
# y = register()
# print(y)



# def get_weekday():
#     cur_date = date.today()
#     weekday = calendar.day_name[cur_date.weekday()].lower()
#     return weekday
#
#
# print(get_weekday())

# x = db.get_employee_id(2)
# print(x['id'])
#
# emp_id = db.get_employee_id(2)
# print(emp_id['id'])
#
# x = db.get_salary_log()
# print(x)

# admin_login
# x = db.fetch_attendance_logs()
# #
# for i in x:
#     print(i)


# def get_user_log(id):
#     x = db.fetch_attendance_logs()
#     c = []
#
#     for i in x:
#         # if i['user'] == id:
#             c.append(i)
#             print(i)
#     print(len(c))
#
#
# get_user_log(2)

# record_attendance
# cmd = 'clock-out'
# x = db.record_attendance(2, cmd, 'longview048')
# h = db.record_attendance(3, cmd, 'longview048')
# print(x)
# print(h)

# dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print(dt)

# x = dataSetCreator.DataSetCreator(0, 12, 100, 'dataSetsample')
#
# x = Identifier.Detect(0)
#
#
# print(x.identify())
#
# print(date.today())

# def ppp(xxx):
#     print(xxx)
#
#
# schedule.every(1).seconds.do(lambda :ppp('fff'))
#
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)



#

# x1 = list(range(1,5))
# x2 = list(range(21, 32))
# xfirst = x2 + x1
#
# xsecond = list(range(5, 21))
#
# print(xsecond)
#
# print(xfirst)
#
# z = datetime(2018, 1, 2, 1, 23, 23, 0) < datetime(2018, 1, 2, 00, 23, 23, 0)

# def leap_year_check(yyy):
#     cur_year = yyy
#     if cur_year % 4 != 0:
#         return False
#     elif cur_year % 100 != 0:
#         return True
#     elif cur_year % 400 != 0:
#         return False
#     else:
#         return True
#
#
# print(leap_year_check(2018))

# now = datetime.now()
# print(now)
#
# start_time = now.replace(hour=5, minute=0, second=0, microsecond=0)
# print(start_time)
# end_time = now.replace(hour=20, minute=0, second=0, microsecond=0)
# print(end_time)
#
#
#
#
#
# if start_time > now and now > end_time:
#     print('cant')
# else:
#     print('can')

# content = {
#     "first_cutoff": 15,
#     "second_cutoff": 30,
#     "level_1_rate": 150,
#     "level_2_rate": 200,
#     "level_3_rate": 200,
#     "overtime_rate": 1.25,
#     "pagibig_pay_day": 30,
#     "philhealth_pay_day": 30,
#     "sss_pay_day": 15,
#     "tax_pay_day": 30
# }
#
# x = db.update_global_conf(content)
# print(x)
#
# content = {
#         'id': 2,
#         'first_name': 'jolo',
#         'middle_name': 'cuizon',
#         'last_name': 'domingo',
#         'position': 'instructor',
#         'is_admin': False,
#         'rate_per_hour': 200.0,
#         'non_working_days': 'sunday, tuesday',
#         'birthday': '2000-04-08',
#         'address': 'gapan',
#         'gender': 'female',
#         'height': 143,
#         'contact_number': '9951079021',
#         "sss_number": "3242-2342342-4234",
#         "pagibig_number": "3242-4234-2342",
#         "philhealth_number": "23-423423423-2",
#         "tin_number": "324-432-423-23423",
#     }
#
#
# x = db.update_employee(content)
# print(x)



# x = db.update_status(3)
#
# if x == 'Employee\'s status was updated':
#     print('ok')
#     print(x)

# def get_attendance_stat():
#     db = EMS_db_model()
#     logs = db.get_salary_log()
#     period = []
#     attendances = []
#     absences = []
#     for k, v in groupby(logs, key=lambda x:x['period']):
#         vlistA = []
#         vlistB = []
#         splitter = k.split('/')
#         k = splitter[2].split(' ')[2][2:] + '.' + splitter[3] + '.' + splitter[4]
#         for i in list(v):
#             vlistA.append(i['days_present'])
#             vlistB.append(i['days_absent'])
#         vlistA = sum(vlistA)/len(vlistA)
#         vlistB = sum(vlistB)/len(vlistB)
#         period.append(k)
#         attendances.append(vlistA)
#         absences.append(vlistB)
#     logs_dict = {
#         'key': period,
#         'attendance_ave': attendances,
#         'absence_ave': absences
#     }
#     return logs_dict
#
#
# print(get_attendance_stat())

# x = 'sunday, tuesday'
#
# print(x.split(','))

print(db.record_attendance(2, 'clock-out', 'longview048'))
print(db.record_attendance(3, 'clock-out', 'what the fuck'))

# x = db.master_verify('qzwxecdsa')
# print(x)