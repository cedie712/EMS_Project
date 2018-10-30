from PyQt4 import QtGui, QtCore
import SalaryView
from models import EMS_db_model
from dateutil.parser import parse
import pytz
time_zone = pytz.timezone('Asia/Manila')
from functools import partial
import spfunc as sp


class SalaryWindow(QtGui.QMainWindow, SalaryView.Ui_SalaryWindow):
    def __init__(self, user_id, parent=None):
        super(SalaryWindow, self).__init__(parent)
        self.setupUi(self)
        fg = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())
        self.setFixedSize(self.size())
        self.statusBar().setVisible(False)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.netpay_frame.setVisible(False)

        self.scrollArea.setWidgetResizable(True)
        self.scrollContent = QtGui.QWidget(self.scrollArea)
        self.scrollLayout = QtGui.QVBoxLayout(self.scrollContent)
        self.scrollLayout.setAlignment(QtCore.Qt.AlignTop)
        self.scrollContent.setLayout(self.scrollLayout)

        self.user_id = user_id
        self.emp_logs = self.fetch_salary_logs()


        for i in self.emp_logs[::-1]:
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
            btn_link.setStyleSheet("QPushButton { text-align: left; }")
            btn_link.clicked.connect(partial(self.populate_report, i['id'], btn_text))
            self.scrollLayout.addWidget(btn_link)
            self.scrollArea.setWidget(self.scrollContent)

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
        self.lbl_days_present.setText('No. of Days Present: ')
        self.lbl_days_absent.setText('No. of Days Absent: ')
        self.lbl_sss.setText('SSS Contirbution: PHP ')
        self.lbl_philhealth.setText('PHILHEALTH Contribution: PHP ')
        self.lbl_pagibig.setText('PAG-IBIG contribution: PHP ')
        self.lbl_tax.setText('Tax: PHP ')
        self.lbl_total_deductions.setText('Total: PHP ')
        self.lbl_special_pay.setText('Special Pay: PHP ')
        self.lbl_gross_pay.setText('Gross Pay: PHP ')
        self.lbl_period.setText('Period: ')
        self.lbl_status.setText('Status: ')
        self.lbl_net_pay.setText('Net Pay: PHP ')

        self.lbl_total_time.setText(self.lbl_total_time.text() + \
                                    label_color % str(selected_log['total_time']))

        self.lbl_days_present.setText(self.lbl_days_present.text() + \
                                      label_color % str(selected_log['days_present']))

        self.lbl_days_absent.setText(self.lbl_days_absent.text() + \
                                     label_color % str(selected_log['days_absent']))

        self.lbl_sss.setText(self.lbl_sss.text() + \
                             label_color % str(round(selected_log['sss_contrib'], 2)))

        self.lbl_philhealth.setText(self.lbl_philhealth.text() + \
                                    label_color % str(round(selected_log['sss_contrib'], 2)))

        self.lbl_pagibig.setText(self.lbl_pagibig.text() + \
                                 label_color % str(round(selected_log['pagibig_contrib'], 2)))

        self.lbl_tax.setText(self.lbl_tax.text() + \
                             label_color % str(round(selected_log['tax'], 2)))

        total_deds = str(round(sum([selected_log['sss_contrib'], selected_log['sss_contrib'],
                                    selected_log['sss_contrib'], selected_log['tax']]), 2))

        self.lbl_total_deductions.setText(self.lbl_total_deductions.text() + label_color % total_deds)

        self.lbl_special_pay.setText(self.lbl_special_pay.text() + \
                                     label_color % str(round(selected_log['special_pay'], 2)))

        self.lbl_gross_pay.setText(self.lbl_gross_pay.text() + \
                                   label_color % str(round(selected_log['gross_pay'], 2)))

        self.lbl_period.setText(self.lbl_period.text() + label_color % period)

        status_text = self.lbl_status.text() + lbl_text_warning % 'Current'
        if selected_log['is_released']:
            status_text = self.lbl_status.text() + lbl_text_green % 'Released'
        self.lbl_status.setText(status_text)

        if selected_log['net_pay'] > 0:
            self.netpay_frame.setVisible(True)

        self.lbl_net_pay.setText(self.lbl_net_pay.text() +\
                                 lbl_text_green % str(round(selected_log['net_pay'], 2)))