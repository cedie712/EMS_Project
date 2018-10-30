import requests
from datetime import datetime, date
from requests.auth import HTTPBasicAuth
import json


class EMS_db_model:
    def __init__(self):

        # API URLs
        self.host = 'http://localhost:8000/'

        self.employeeURL = self.host + 'Employee/'
        self.employeeConfigURL = self.host + 'EmployeeConfig/'
        self.employeeProfileURL = self.host + 'EmployeeProfile/'
        self.employeeScheduleURL = self.host + 'EmployeeSchedule/'
        self.attendanceLogURL = self.host + 'AttendanceLog/'
        self.salaryReportURL = self.host + 'SalaryReport/'
        self.globalConfigURL = self.host + 'GlobalConfig/'

        self.registerURL = self.host + 'registerEmployee/'
        self.adminVerify = self.host + 'adminVerify/'
        self.recordAttendance = self.host + 'recordAttendance/'
        self.getUserInfo = self.host + 'userInfo/'
        self.updateGlobalConfig = self.host + 'updateGlobalConfig/'
        self.updateEmployee = self.host + 'updateEmployee/'
        self.updateStatus = self.host + 'updateStatus/'

        # Http Authentication
        self.user = 'cedrick'
        self.password = 'ChangeMeYouBastard'
        self.auth = HTTPBasicAuth(self.user, self.password)

        # get configurations
        self.config = self.get_config()[0]

    def get_config(self):
        configurations = requests.get(self.globalConfigURL, auth=self.auth)
        return configurations.json()

    def register_user(self, data):
        if int(data['birthday'].split('-')[0]) > (int(str(date.today()).split('-')[0]) - 18):
            return 'you are not yet at the proper age of working'

        if data['password'] != data['confirm']:
            return 'passwords didn\'t match'


        birthday = datetime.strptime(data['birthday'], "%Y-%m-%d").date()

        gmail = data['email'] + '@gmail.com'

        rate = float(data['rate'])


        content = {
            # user
            "username": data['username'],
            "password": data['password'],
            "email": gmail,

            # employee_object
            "user": data['username'],
            "first_name": data['fname'],
            "middle_name": data['mname'],
            "last_name": data['lname'],
            "position": data['position'],
            "is_admin": data['is_admin'],
            "is_active": True,

            # employee_config
            "sss_number": data['sss_number'],
            "pagibig_number": data['pagibig_number'],
            "philhealth_number": data['philhealth_number'],
            "tin_number": data['tin_number'],
            "rate_per_hour": rate,
            "non_working_days": data['day_off'],

            # employee_profile
            "address": "gapan",
            "birthday": birthday,
            "gender": data['gender'],
            "height": data['height'],
            "contact_number": data['contact_number'],
        }

        save_data = requests.post(self.registerURL, data=content, auth=self.auth)
        return save_data.json()

    def admin_verify(self, userid, password):
        """use face identification to validate who the shit he is"""
        content = {'user': userid, 'password': password}
        validate_user = requests.get(self.adminVerify, data=content, auth=self.auth)
        return validate_user.json()

    def master_verify(self, password):
        if password == self.password:
            return True
        return False

    def record_attendance(self, user_id, command, password):
        content = {'user_id': user_id,
                   'command': command,
                   'password': password}
        record = requests.post(self.recordAttendance, data=content, auth=self.auth)
        return record.json()

    def fetch_attendance_logs(self):
        log = requests.get(self.attendanceLogURL, auth=self.auth)
        return log.json()

    def fetch_profile(self):
        profile = requests.get(self.employeeURL, auth=self.auth)
        return profile.json()

    def fetch_profile_ext(self):
        profile = requests.get(self.employeeProfileURL, auth=self.auth)
        return profile.json()

    def fetch_profile_config(self):
        profile = requests.get(self.employeeConfigURL, auth=self.auth)
        return profile.json()

    def get_employee_id(self, user_id):
        employees = requests.get(self.employeeURL, auth=self.auth)
        employee_dicts = employees.json()

        for i in employee_dicts:
            if i['user'] == user_id:
                return i

    def get_user_info(self, emp_id):
        content = {'emp_id': emp_id}
        user_info = requests.get(self.getUserInfo, data=content, auth=self.auth)
        return  user_info.json()

    def get_salary_log(self):
        logs = requests.get(self.salaryReportURL, auth=self.auth)
        return logs.json()

    def update_global_conf(self, content):
        update_conf = requests.post(self.updateGlobalConfig, data=content, auth=self.auth)
        return update_conf.json()

    def update_employee(self, content):
        update_emp = requests.post(self.updateEmployee, data=content, auth=self.auth)
        return update_emp.json()

    def update_status(self, emp_id):
        content = {'id': emp_id}
        update_emp = requests.post(self.updateStatus, data=content, auth=self.auth)
        return  update_emp.json()

    def get_forgot_pass_link(self):
        return self.host + 'accounts/password_reset/'