from PyQt4 import QtGui, QtCore
from Attendance import AttendanceWindow
import config
from Salary import SalaryWindow
import EmployeeView
from models import EMS_db_model
import spfunc as sp
from datetime import datetime
from dateutil.parser import parse
import pytz
from functools import partial
time_zone = pytz.timezone('Asia/Manila')
import cv2
from face import dataSetCreator
from datasetcheck import CaptureCheckWindow
from printdata import create_pdf

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class ProfileWindow(QtGui.QMainWindow, EmployeeView.Ui_EmployeeView):
    def __init__(self, user_id, parent=None):
        super(ProfileWindow, self).__init__(parent)
        self.setupUi(self)
        fg = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())
        self.setFixedSize(self.size())
        self.statusBar().setVisible(False)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.birthday_txt.setCalendarPopup(True)
        self.print_btn.setVisible(False)
        self.data_to_print = None

        self.user_id = user_id
        self.db = EMS_db_model()
        self.setUp_profile()

        self.attendancelog_btn.clicked.connect(self.show_attendance_view)
        self.update_btn.clicked.connect(self.update_employee)
        self.train_btn.clicked.connect(self.capture_dataset)
        self.print_btn.clicked.connect(self.gen_pdf)

        # # # SALARY # # #
        self.netpay_frame.setVisible(False)

        self.scrollArea.setWidgetResizable(True)
        self.scrollContent = QtGui.QWidget(self.scrollArea)
        self.scrollLayout = QtGui.QVBoxLayout(self.scrollContent)
        self.scrollLayout.setAlignment(QtCore.Qt.AlignTop)
        self.scrollContent.setLayout(self.scrollLayout)

        self.user_id = user_id
        self.emp_logs = self.fetch_salary_logs()

        for i in self.emp_logs:
            btn_text = '  Current'
            if i['is_released']:
                start_date = i['period'].split(' - ')[0]
                start_date = parse(start_date)
                start_date = start_date.strftime("%b %d, %Y")
                end_date = i['period'].split(' - ')[1]
                end_date = parse(end_date)
                end_date = end_date.strftime("%b %d, %Y")
                btn_text = "  %s - %s" % (start_date, end_date)
            btn_link = QtGui.QPushButton(btn_text, self.scrollArea)
            btn_link.setStyleSheet("text-align: left;\n color: #fff;\n"
                                   "background-color: rgb(5, 101, 255);")
            btn_link.clicked.connect(partial(self.populate_report, i['id'], btn_text))
            self.scrollLayout.addWidget(btn_link)
            self.scrollArea.setWidget(self.scrollContent)
        # # # SALARY # # #

    # # # PROFILE # # #
    def fetch_employee(self):
        employee = self.db.fetch_profile()
        for i in employee:
            if i['id'] == self.user_id:
                return i

    def fetch_profile(self):
        employee_profile = self.db.fetch_profile_ext()
        for i in employee_profile:
            if i['user'] == self.user_id:
                return i

    def fetch_config(self):
        employee_config = self.db.fetch_profile_config()
        for i in employee_config:
            if i['user'] == self.user_id:
                return i

    def setUp_profile(self):
        emp = self.fetch_employee()
        userx = self.db.get_user_info(emp['user'])
        profile = self.fetch_profile()
        config = self.fetch_config()

        label_color = "<font color='#0f7a62'>%s</font>"
        lbl_text_green = "<font color='green'>%s</font>"
        lbl_text_warning = "<font color='orangered'>%s</font>"
        lbl_text_red = "<font color='red'>%s</font>"
        # font_style = "QLabel {font: Arial}"

        # Profile Information
        if emp['is_active'] is False:
            status = 'Inactive'
            self.lbl_status.setText(self.lbl_status.text() + lbl_text_red % status)
        else:
            status = 'Active'
            self.lbl_status.setText(self.lbl_status.text() + lbl_text_green % status)

        # self.lbl_status.setStyleSheet(font_style)

        self.lbl_username.setText(self.lbl_username.text() + label_color % userx[0])

        self.lbl_name_2.setText(self.lbl_name_2.text() + \
                                lbl_text_green % '%s, %s %s'.capitalize() %
                                (emp['last_name'], emp['first_name'], emp['middle_name']))

        self.name_full = '%s, %s %s'.capitalize() % (emp['last_name'], emp['first_name'], emp['middle_name'])

        self.lbl_id.setText(self.lbl_id.text() + \
                            lbl_text_green % sp.convert_id(emp['id'], emp['start_date'][:4]))

        birthday = parse(profile['birthday']).astimezone(time_zone)
        birthday = birthday.strftime("%b %d, %Y")

        self.lbl_bday.setText(self.lbl_bday.text() + label_color % birthday)

        self.lbl_gender.setText(self.lbl_gender.text() + label_color % profile['gender'].capitalize())

        self.lbl_address.setText(self.lbl_address.text() + \
                                 label_color % "<font size=2>%s</font>" % profile['address'].capitalize())

        self.lbl_gmail.setText(self.lbl_gmail.text() + label_color % "<font size=2>%s</font>" % userx[1])

        self.lbl_contact.setText(self.lbl_contact.text() + label_color % profile['contact_number'])
        # self.lbl_contact.setStyleSheet(font_style)

        self.lbl_height.setText(self.lbl_height.text() + label_color % str(profile['height']))

        age = int(datetime.now().strftime('%Y')) - int(profile['birthday'][:4])
        self.lbl_age.setText(self.lbl_age.text() + label_color % str(age))

        date_joined = parse(emp['start_date']).astimezone(time_zone)
        date_joined = date_joined.strftime("%b %d, %Y")

        self.lbl_start_date.setText(self.lbl_start_date.text() + label_color % date_joined)

        self.lbl_presence_count.setText(self.lbl_presence_count.text() + \
                                        lbl_text_green % str(profile['presences_count']))

        abstext_color = lbl_text_green
        if profile['absences_count'] > 0:
            abstext_color = lbl_text_warning

        elif profile['absences_count'] > 10:
            abstext_color = lbl_text_red

        self.lbl_absence_count.setText(self.lbl_absence_count.text() + \
                                       abstext_color % str(profile['absences_count']))

        # Job Information
        self.lbl_position.setText(self.lbl_position.text() + label_color % emp['position'].capitalize())
        self.position = emp['position']

        self.lbl_rate.setText(self.lbl_rate.text() + label_color % "PHP %s/hour" % str(config['rate_per_hour']))

        self.lbl_dayoff.setText(self.lbl_dayoff.text() + label_color % config['non_working_days'])

        self.lbl_sss.setText(self.lbl_sss.text() + label_color % config['sss_number'])

        self.lbl_philhealth.setText(self.lbl_philhealth.text() + label_color % config['philhealth_number'])

        self.lbl_pagibig.setText(self.lbl_pagibig.text() + label_color % config['pagibig_number'])

        self.lbl_tin.setText(self.lbl_tin.text() + label_color % config['tin_number'])


        self.lbl_profile_photo.setPixmap(QtGui.QPixmap(_fromUtf8("profilepics/%s.png" % str(userx[2]))))
        self.lbl_profile_photo.setScaledContents(True)
        self.lbl_profile_photo.setObjectName(_fromUtf8("lbl_profile_photo"))

        # populate update text boxes
        self.fname_txt.setText(emp['first_name'].capitalize())
        self.mname_txt.setText(emp['middle_name'].capitalize())
        self.lname_txt.setText(emp['last_name'].capitalize())
        self.contact_txt.setText(profile['contact_number'])
        self.address_txt.setText(profile['address'].capitalize())
        bday = profile['birthday'].split('-')
        self.birthday_txt.setDate(QtCore.QDate(int(bday[0]), int(bday[1]), int(bday[2])))

        self.male_radio.setChecked(True)
        if profile['gender'] != 'male':
            self.female_radio.setChecked(True)
        self.height_txt.setText(str(profile['height']))

        self.active_radio.setChecked(True)
        if emp['is_active'] is False:
            self.inactive_radio.setChecked(True)

        if 'monday' in config['non_working_days']:
            self.checkBox_mon.setChecked(True)
        if 'tuesday' in config['non_working_days']:
            self.checkBox_tue.setChecked(True)
        if 'wednesday' in config['non_working_days']:
            self.checkBox_wed.setChecked(True)
        if 'thursday' in config['non_working_days']:
            self.checkBox_thu.setChecked(True)
        if 'friday' in config['non_working_days']:
            self.checkBox_fri.setChecked(True)
        if 'saturday' in config['non_working_days']:
            self.checkBox_sat.setChecked(True)

        position_lists = ['instructor', 'administrator']
        for i in position_lists:
            self.position_combo.addItem(i)
        if emp['is_admin']:
            self.position_combo.setCurrentIndex(1)

        global_conf = self.db.get_config()[0]

        rates_list = [global_conf['level_1_rate'], global_conf['level_2_rate'], global_conf['level_3_rate']]
        for i in range(3):
            self.rate_combo.addItem('PHP ' + str(rates_list[i]))
            if config['rate_per_hour'] == rates_list[i]:
                self.rate_combo.setCurrentIndex(i)

        self.sss_txt.setText(config['sss_number'])
        self.philhealth_txt.setText(config['philhealth_number'])
        self.pagibig_txt.setText(config['pagibig_number'])
        self.tin_txt.setText(config['tin_number'])

        regex_letter = QtCore.QRegExp("([a-zA-Z]+[ ])+")
        validator_letter = QtGui.QRegExpValidator(regex_letter)

        regex_contact = QtCore.QRegExp("^9(?!(000000000))\d{9}$")
        validator_contact = QtGui.QRegExpValidator(regex_contact)

        regex_sss = QtCore.QRegExp("^(?!(00))\d{2}-(?!(000000000))\d{9}-(?!(0))\d{1}$")
        validator_sss = QtGui.QRegExpValidator(regex_sss)

        regex_philhealth = QtCore.QRegExp("^(?!(00))\d{2}-(?!(000000000))\d{9}-(?!(0))\d{1}$")
        validator_philhealth = QtGui.QRegExpValidator(regex_philhealth)

        regex_pagibig = QtCore.QRegExp("^(?!(0000))\d{4}-(?!(0000))\d{4}-(?!(0000))\d{4}$")
        validator_pagibig = QtGui.QRegExpValidator(regex_pagibig)

        regex_tin = QtCore.QRegExp("^(?!(000))\d{3}-(?!(000))\d{3}-(?!(000))\d{3}-(?!(00000))\d{5}$")
        validator_tin = QtGui.QRegExpValidator(regex_tin)

        regex_height = QtCore.QRegExp("^1(?!([1, 2, 9, 0]))\d{1}(?!(0))\d{1}$")
        validator_height = QtGui.QRegExpValidator(regex_height)

        self.fname_txt.setValidator(validator_letter)
        self.fname_txt.setMaxLength(35)
        self.mname_txt.setValidator(validator_letter)
        self.mname_txt.setMaxLength(35)
        self.lname_txt.setValidator(validator_letter)
        self.lname_txt.setMaxLength(35)

        self.height_txt.setValidator(validator_height)
        self.contact_txt.setValidator(validator_contact)
        self.sss_txt.setValidator(validator_sss)
        self.philhealth_txt.setValidator(validator_philhealth)
        self.pagibig_txt.setValidator(validator_pagibig)
        self.tin_txt.setValidator(validator_tin)



    def show_attendance_view(self):
        all_logs = self.db.fetch_attendance_logs()
        user_log = []
        for i in all_logs:
            if i['user'] == self.user_id:
                user_log.append(i)
        attendancewindow = AttendanceWindow(user_log, self)
        attendancewindow.show()

    def show_salary_view(self):
        salarywindow = SalaryWindow(self.user_id, self)
        salarywindow.show()
    # # # PROFILE # # #

    # # # SALARY # # #
    def fetch_salary_logs(self):
        db = EMS_db_model()
        all_logs = db.get_salary_log()
        emp_log = []
        for i in all_logs:
            if i['user'] == self.user_id:
                emp_log.append(i)
        return emp_log

    def populate_report(self, log_id, period):
        salary_log = self.fetch_salary_logs()
        report = []
        for i in salary_log:
            if i['id'] == log_id:
                report.append(i)
                break
        selected_log = report[0]

        # labels
        label_color = "<font color='#0f7a62'>%s</font>"
        lbl_text_green = "<font color='green'>%s</font>"
        lbl_text_warning = "<font color='orangered'>%s</font>"

        self.netpay_frame.setVisible(False)
        self.lbl_total_time.setText('Total Time: ')
        self.lbl_total_ot.setText('Total Over Time: ')
        self.lbl_days_present.setText('No. of Days Present: ')
        self.lbl_days_absent.setText('No. of Days Absent: ')
        self.lbl_sss_2.setText('SSS Contirbution: PHP ')
        self.lbl_philhealth_2.setText('PHILHEALTH Contribution: PHP ')
        self.lbl_pagibig_2.setText('PAG-IBIG contribution: PHP ')
        self.lbl_tax.setText('Tax: PHP ')
        self.lbl_total_deductions.setText('Total: PHP ')
        self.lbl_special_pay.setText('Special Pay: PHP ')
        self.lbl_gross_pay.setText('Gross Pay: PHP ')
        self.lbl_period.setText('Period: ')
        self.lbl_status_2.setText('Status: ')
        self.lbl_net_pay.setText('Net Pay: PHP ')

        self.lbl_total_time.setText(self.lbl_total_time.text() + \
                                    label_color % str(selected_log['total_time']))

        self.lbl_total_ot.setText(self.lbl_total_ot.text() + \
                                    label_color % str(selected_log['total_over_time']))

        self.lbl_days_present.setText(self.lbl_days_present.text() + \
                                      label_color % str(selected_log['days_present']))

        self.lbl_days_absent.setText(self.lbl_days_absent.text() + \
                                     label_color % str(selected_log['days_absent']))

        self.lbl_sss_2.setText(self.lbl_sss_2.text() + \
                             label_color % str("{:.2f}".format(selected_log['sss_contrib'])))

        self.lbl_philhealth_2.setText(self.lbl_philhealth_2.text() + \
                                    label_color % str("{:.2f}".format(selected_log['sss_contrib'])))

        self.lbl_pagibig_2.setText(self.lbl_pagibig_2.text() + \
                                 label_color % str("{:.2f}".format(selected_log['pagibig_contrib'])))

        self.lbl_tax.setText(self.lbl_tax.text() + \
                             label_color % str("{:.2f}".format(selected_log['tax'])))

        total_deds = str("{:.2f}".format(sum([selected_log['sss_contrib'], selected_log['sss_contrib'],
                                    selected_log['sss_contrib'], selected_log['tax']])))

        self.lbl_total_deductions.setText(self.lbl_total_deductions.text() + label_color % total_deds)

        self.lbl_special_pay.setText(self.lbl_special_pay.text() + \
                                     label_color % str("{:.2f}".format(selected_log['special_pay'])))

        self.lbl_gross_pay.setText(self.lbl_gross_pay.text() + \
                                   label_color % str("{:.2f}".format(selected_log['gross_pay'])))

        self.lbl_period.setText(self.lbl_period.text() + label_color % period)

        status_text = self.lbl_status_2.text() + lbl_text_warning % 'Current'
        stat = 'Current'
        if selected_log['is_released']:
            status_text = self.lbl_status_2.text() + lbl_text_green % 'Released'
            stat = 'Released'
        self.lbl_status_2.setText(status_text)

        if selected_log['net_pay'] > 0:
            self.netpay_frame.setVisible(True)

        self.lbl_net_pay.setText(self.lbl_net_pay.text() +\
                                 lbl_text_green % str("{:.2f}".format(selected_log['net_pay'])))
        self.print_btn.setVisible(True)

        self.data_to_print = {
            'title': self.name_full.replace(' ', '') + '-' +
                     datetime.now().strftime("%B %d, %Y %I:%M:%S %p") + '-' + period,
            'current_date': datetime.now().strftime("%B %d, %Y %I:%M:%S %p"),
            'total_time': str(selected_log['total_time']),
            'total_overtime': str(selected_log['total_over_time']),
            'days_present': str(selected_log['days_present']),
            'days_absent': str(selected_log['days_absent']),
            'sss': str("{:.2f}".format(selected_log['sss_contrib'])),
            'philhealth': str("{:.2f}".format(selected_log['philhealth_contrib'])),
            'pagibig': str("{:.2f}".format(selected_log['pagibig_contrib'])),
            'tax': str("{:.2f}".format(selected_log['tax'])),
            'total_ded': total_deds,
            'special_pay': str("{:.2f}".format(selected_log['special_pay'])),
            'gross_pay': str("{:.2f}".format(selected_log['gross_pay'])),
            'period': period,
            'status': stat,
            'net_pay': str("{:.2f}".format(selected_log['net_pay'])),
            'name': self.name_full,
            'position': self.position
        }

        # # # SALARY # # #

    # # # Generate and Print PDF # # #
    def gen_pdf(self):
        create_pdf(self.data_to_print)
        return  QtGui.QMessageBox.warning(self, 'Note', 'PDF file was generated.'
                                                        ' Silent print job was sent on process', None)
    # # # Generate and Print PDF # # #


    # # # Update User Info and Config # # #
    def update_employee(self):
        emp = self.fetch_employee()
        profile = self.fetch_profile()
        config = self.fetch_config()

        position = str(self.position_combo.currentText())
        rate = float(self.rate_combo.currentText().split(' ')[1])
        dayoff = 'sunday'

        if self.checkBox_mon.isChecked():
            dayoff += ', monday'
        if self.checkBox_tue.isChecked():
            dayoff += ', tuesday'
        if self.checkBox_wed.isChecked():
            dayoff += ', wednesday'
        if self.checkBox_thu.isChecked():
            dayoff += ', thursday'
        if self.checkBox_fri.isChecked():
            dayoff += ', friday'
        if self.checkBox_sat.isChecked():
            dayoff += ', saturday'

        is_admin = False
        if position == 'administrator':
            is_admin = True

        gender = 'male'
        if self.female_radio.isChecked():
            gender = 'female'

        status_value = True
        if self.inactive_radio.isChecked():
            status_value = False

        birthday = datetime.strptime(self.birthday_txt.text(), "%Y-%m-%d").date()

        if self.fname_txt.text().lower() == emp['first_name'].lower() \
                and self.mname_txt.text().lower() == emp['middle_name'].lower() \
                and self.lname_txt.text().lower() == emp['last_name'].lower() \
                and self.contact_txt.text() == profile['contact_number'] \
                and self.address_txt.text().lower() == profile['address'].lower() \
                and str(birthday) == str(profile['birthday']) \
                and self.height_txt.text() == str(profile['height']) \
                and gender == profile['gender'] \
                and status_value == emp['is_active'] \
                and position == emp['position'] \
                and rate == config['rate_per_hour'] \
                and dayoff == config['non_working_days'] \
                and self.sss_txt.text() == config['sss_number'] \
                and self.philhealth_txt.text() == config['philhealth_number'] \
                and self.pagibig_txt.text() == config['pagibig_number'] \
                and self.tin_txt.text() == config['tin_number']:
            QtGui.QMessageBox.information(self, 'Note', 'you did not made any changes', None)
            return 0

        input_fields = [self.fname_txt.text(), self.mname_txt.text(), self.lname_txt.text(),
                        self.contact_txt.text(), self.height_txt.text(), self.sss_txt.text(),
                        self.philhealth_txt.text(), self.pagibig_txt.text(), self.tin_txt.text(),
                        self.address_txt.text()]

        if any(i == '' or i == None for i in input_fields):
            QtGui.QMessageBox.information(self, 'Note', 'complete the fields', None)
            return 0

        if len(self.contact_txt.text()) != 10:
            title = 'Failed'
            msg = 'Please enter a correct contact number. eg. 9xxxxxxxxx'
            return QtGui.QMessageBox.information(self, title, msg, None)

        content = {
            'id': self.user_id,
            'first_name': self.fname_txt.text(),
            'middle_name': self.mname_txt.text(),
            'last_name': self.lname_txt.text(),
            'position': position,
            'is_admin': is_admin,
            'is_active': status_value,
            "sss_number": self.sss_txt.text(),
            "pagibig_number": self.pagibig_txt.text(),
            "philhealth_number": self.philhealth_txt.text(),
            "tin_number": self.tin_txt.text(),
            'rate_per_hour': rate,
            'non_working_days': dayoff,
            'birthday': birthday,
            'address': self.address_txt.text(),
            'gender': gender,
            'height': self.height_txt.text(),
            'contact_number': self.contact_txt.text(),
        }

        title_failed = 'Failed'

        if len(self.height_txt.text()) != 3:
            title = 'Failed'
            msg = 'Incorrect height value'
            return QtGui.QMessageBox.information(self, title, msg, None)

        if len(self.sss_txt.text()) != 14:
            msg = 'Incorrect SSS number'
            QtGui.QMessageBox.information(self, title_failed, msg, None)
            return 0
        elif len(self.philhealth_txt.text()) != 14:
            msg = 'Incorrect PHILHEALTH number'
            QtGui.QMessageBox.information(self, title_failed, msg, None)
            return 0
        elif len(self.pagibig_txt.text()) != 14:
            msg = 'Incorrect PAGIBIG number'
            QtGui.QMessageBox.information(self, title_failed, msg, None)
            return 0
        elif len(self.tin_txt.text()) < 16:
            msg = 'Incorrect TIN number'
            QtGui.QMessageBox.information(self, title_failed, msg, None)
            return 0
        else:
            update = self.db.update_employee(content)

            if update == 'nice mother fucker':
                title_success = 'Success'
                msg = 'employee\'s information and configurations are updated'
                QtGui.QMessageBox.information(self, title_success, msg, None)
                self.hide()
                return 0
            else:
                msg = 'something went wrong, please check internet connection'
                QtGui.QMessageBox.information(self, title_failed, msg, None)
                return 0
    # # # Update User Info and Config # # #

    # # # Update Face Data Set # # #
    def capture_dataset(self):
        emp = self.fetch_employee()
        userx = self.db.get_user_info(emp['user'])
        self.setEnabled(False)
        dataSetCreator.DataSetCreator(config.CAMERA_INDEX, int(userx[2]), 1, 'dataSetsample')
        check_if_ok = CaptureCheckWindow(int(userx[2]), self)
        if not check_if_ok.exec_():
            check_if_ok.hide()
        else:
            pass
        cv2.destroyAllWindows()
        self.setEnabled(True)
        msg = 'Face data sets are updated'
        QtGui.QMessageBox.information(self, 'Note', msg, None)
        return 0
    # # # Update Face Data Set # # #


