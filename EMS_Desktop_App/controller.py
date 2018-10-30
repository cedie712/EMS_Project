import sys
import cv2
from PyQt4 import QtGui, QtCore
# from speechProcess import Speech
from datetime import datetime, date
# import threading
import authenticatecd
import Home, authentication_form
from Memo import MemoWindow
from help import HelpWindow
from graph import GraphOpt
from Registration import RegisterWindow
from employeelisting import EmployeeListView
from clockedemployee import ClockedEmployeeWindow
from GlobalConfig import GlobalConfigWindow
from face import Identifier, dataSetCreator
from models import EMS_db_model
from dateutil.parser import parse
import pytz
time_zone = pytz.timezone('Asia/Manila')
import spfunc as sp
import time


class MainWindow(QtGui.QMainWindow, Home.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.statusBar().setVisible(False)
        self.btn_close.setVisible(False)
        self.user_pass.setEchoMode(QtGui.QLineEdit.Password)
        self.user_pass.setMaxLength(35)
        self.search_lineEdit.setVisible(False)
        self.search_lineEdit_2.setVisible(False)
        self.label_search.setVisible(False)

        time_timer = QtCore.QTimer(self)
        time_timer.timeout.connect(self.update_time)
        time_timer.start(1000)

        # test
        # self.btn_signin.clicked.connect(self.capture_thread)
        # self.btn_receiver.clicked.connect(self.show_logs)
        # self.btn_receiver.clicked.connect(self.capture_voice)

        self.btn_signin.clicked.connect(self.sign_in)
        self.btn_signin.setShortcut('Ctrl+I')
        self.btn_signout.clicked.connect(self.sign_out)
        self.btn_signout.setShortcut('Ctrl+O')
        self.btn_logs.clicked.connect(self.log_request)
        self.btn_logs.setShortcut('Ctrl+S')
        self.btn_alllogs.clicked.connect(self.all_log_request)
        self.btn_alllogs.setShortcut('Ctrl+A')
        self.btn_help.clicked.connect(self.help_show)
        self.btn_help.setShortcut('F1')

        self.register_toolbtn.clicked.connect(self.register_window_show)
        self.register_toolbtn.setShortcut('Ctrl+R')
        self.employeeinfo_toolbtn.clicked.connect(self.employee_list_show)
        self.employeeinfo_toolbtn.setShortcut('Ctrl+Y')
        self.settings_toolbtn.clicked.connect(self.edit_config_show)
        self.settings_toolbtn.setShortcut('Ctrl+W')
        self.clocked_toolbtn.clicked.connect(self.clocked_employee_show)
        self.clocked_toolbtn.setShortcut('Ctrl+T')
        self.charts_toolbtn.clicked.connect(self.graphopt_show)
        self.charts_toolbtn.setToolTip('graphs')
        self.charts_toolbtn.setShortcut('Ctrl+G')
        self.memo_toolbtn.clicked.connect(self.memo_show)
        self.memo_toolbtn.setToolTip('memo')
        self.memo_toolbtn.setShortcut('Ctrl+M')

        self.btn_close.clicked.connect(self.clear_pane)

        # table
        self.attendance_view.setColumnCount(2)
        self.attendance_view.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.attendance_table_headers = ['Time-In', 'Time-Out']
        self.attendance_view.setHorizontalHeaderLabels(self.attendance_table_headers)
        self.header = self.attendance_view.horizontalHeader()
        self.header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.header.setResizeMode(1, QtGui.QHeaderView.Stretch)

        self.filtering_list = None
        self.search_lineEdit.textChanged.connect(self.filter_table_all_logs)
        self.search_lineEdit_2.textChanged.connect(self.filter_table_singleuser_logs)

        self.show()

    def filter_table_singleuser_logs(self):
        if self.filtering_list is None:
            pass
        else:
            filter_string = self.search_lineEdit_2.text().lower()
            new_logs = []

            for i in self.filtering_list:
                if filter_string in i[0].lower() or filter_string in i[1]:
                    new_logs.append(i)
            row = 0
            self.attendance_view.setRowCount(len(new_logs))

            for i in new_logs:
                self.attendance_view.setItem(row, 0, QtGui.QTableWidgetItem(i[0]))
                self.attendance_view.setItem(row, 1, QtGui.QTableWidgetItem(i[1]))
                row += 1
            self.attendance_view.scrollToBottom()

    def filter_table_all_logs(self):
        if self.filtering_list is None:
            pass
        else:
            filter_string = self.search_lineEdit.text().lower()
            new_logs = []

            for i in self.filtering_list:
                if filter_string in i[0].lower() or filter_string in i[1]\
                        or filter_string in i[2].lower() or filter_string in i[3].lower():
                    new_logs.append(i)
            row = 0
            self.attendance_view.setRowCount(len(new_logs))

            for i in new_logs:
                self.attendance_view.setItem(row, 0, QtGui.QTableWidgetItem(i[0]))
                self.attendance_view.setItem(row, 1, QtGui.QTableWidgetItem(i[1]))
                self.attendance_view.setItem(row, 2, QtGui.QTableWidgetItem(i[2]))
                self.attendance_view.setItem(row, 3, QtGui.QTableWidgetItem(i[3]))
                row += 1
            self.attendance_view.scrollToBottom()


    def clear_pane(self):
        self.attendance_view.setRowCount(0)
        self.name_label.setText('')
        self.btn_close.setVisible(False)
        self.search_lineEdit.setVisible(False)
        self.search_lineEdit_2.setVisible(False)
        self.label_search.setVisible(False)
        self.attendance_table_headers = ['Time-In', 'Time-Out']
        self.attendance_view.setColumnCount(2)


    def show_attendance_logs(self, user_id):
        self.search_lineEdit.setVisible(False)
        self.search_lineEdit_2.setVisible(True)
        self.label_search.setVisible(True)
        self.btn_close.setVisible(True)
        self.attendance_table_headers = ['Time-In', 'Time-Out']
        self.attendance_view.setColumnCount(2)
        self.header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.header.setResizeMode(1, QtGui.QHeaderView.Stretch)

        db = EMS_db_model()
        all_profile = db.fetch_profile()
        for i in all_profile:
            if i['id'] == user_id:
                self.name_label.setText('%s, %s %s  %s' % (i['last_name'], i['first_name'], i['middle_name'],
                                                        'ID:' + sp.convert_id(user_id, i['start_date'][:4])))
        all_logs = db.fetch_attendance_logs()
        user_log = []
        for i in all_logs:
            if i['user'] == user_id:
                user_log.append(i)
        self.attendance_view.setRowCount(len(user_log))

        row = 0
        for_filtering = []
        for i in user_log:
            time_in = parse(i['time_in']).astimezone(time_zone)
            time_in = time_in.strftime("%B %d, %Y %I:%M:%S %p")
            time_out = ' '
            if i['time_out'] is not None:
                time_out = parse(i['time_out']).astimezone(time_zone)
                time_out = time_out.strftime("%B %d, %Y %I:%M:%S %p")
            self.attendance_view.setItem(row, 0, QtGui.QTableWidgetItem(str(time_in)))
            self.attendance_view.setItem(row, 1, QtGui.QTableWidgetItem(str(time_out)))
            row += 1
            for_filtering.append([time_in, time_out])
        self.attendance_view.scrollToBottom()
        self.filtering_list = for_filtering


    def show_all_attendance_logs(self):
        self.search_lineEdit_2.setVisible(False)
        self.search_lineEdit.setVisible(True)
        self.label_search.setVisible(True)
        self.btn_close.setVisible(True)
        db = EMS_db_model()
        all_logs = db.fetch_attendance_logs()

        self.attendance_view.setColumnCount(4)
        self.attendance_table_headers.append('Employee Name')
        self.attendance_table_headers.append('ID')
        self.attendance_view.setHorizontalHeaderLabels(self.attendance_table_headers)
        self.header.setResizeMode(2, QtGui.QHeaderView.Stretch)
        self.attendance_view.setRowCount(len(all_logs))
        row = 0

        for_filtering = []

        all_profile = db.fetch_profile()
        for i in all_logs:
            emp_name = ''
            gcc_id = ''
            for ii in all_profile:
                if ii['id'] == i['user']:
                    gcc_id = sp.convert_id(ii['id'], ii['start_date'][:4])
                    emp_name = '%s, %s %s' % (ii['last_name'], ii['first_name'], ii['middle_name'])
            time_in = parse(i['time_in']).astimezone(time_zone)
            time_in = time_in.strftime("%B %d, %Y %I:%M:%S %p")
            time_out = ' '
            if i['time_out'] is not None:
                time_out = parse(i['time_out']).astimezone(time_zone)
                time_out = time_out.strftime("%B %d, %Y %I:%M:%S %p")
            self.attendance_view.setItem(row, 0, QtGui.QTableWidgetItem(str(time_in)))
            self.attendance_view.setItem(row, 1, QtGui.QTableWidgetItem(str(time_out)))
            self.attendance_view.setItem(row, 2, QtGui.QTableWidgetItem(emp_name))
            self.attendance_view.setItem(row, 3, QtGui.QTableWidgetItem(gcc_id))
            row += 1
            for_filtering.append([time_in, time_out, emp_name, gcc_id])
        self.attendance_view.scrollToBottom()
        self.name_label.setText('')
        self.filtering_list = for_filtering

    def record_attendance(self, command, password):
        authCD = AuthCDWindow(self)
        if not authCD.exec_():
            login.hide()
        else:
            self.setEnabled(False)
            cap = Identifier.Detect(0)
            id = cap.identify()
            cv2.destroyAllWindows()
            self.setEnabled(True)
            db = EMS_db_model()
            if id is False:
                QtGui.QMessageBox.warning(self, 'Note',
                                          'Unknown Person', None)
                self.user_pass.clear()
            if id is None:
                return 0
            authenticate = db.admin_verify(id, password)
            note = 'Invalid Credentials'
            if authenticate is False or authenticate is True:
                record = db.record_attendance(id, command, password)
                note = record[1]
                if note != 'You are not authorized for this action anymore':
                    self.show_attendance_logs(record[0])
            QtGui.QMessageBox.information(self, 'Note',
                                      note, None)
            self.user_pass.clear()
            if note == 'Invalid Credentials':
                self.clear_pane()

    def show_logs(self, command, password):
        authCD = AuthCDWindow(self)
        if not authCD.exec_():
            login.hide()
        else:
            self.setEnabled(False)
            cap = Identifier.Detect(0)
            id = cap.identify()
            cv2.destroyAllWindows()
            self.setEnabled(True)
            db = EMS_db_model()
            if id is False:
                QtGui.QMessageBox.warning(self, 'Note',
                                          'Unknown Person', None)
                self.user_pass.clear()
                return 0
            if id is None:
                self.name_label.setText('')
                return 0
            admin_validate = db.admin_verify(id, password)
            if admin_validate:
                if admin_validate == 'Incorrect Password':
                    self.clear_pane()
                    self.user_pass.clear()
                    return QtGui.QMessageBox.warning(self, 'Note',
                                                     'Invalid Credentials', None)
            if command == 'show my logs':
                emp_id = db.get_employee_id(int(id))
                self.show_attendance_logs(emp_id['id'])
            elif command == 'show all logs':
                if admin_validate is False:
                    self.clear_pane()
                    self.user_pass.clear()
                    return QtGui.QMessageBox.warning(self, 'Note',
                                                     'You are not authorized for this action', None)
                self.show_all_attendance_logs()
            self.user_pass.clear()


    def update_time(self):
        cur_time = datetime.now().strftime('%I:%M:%S %p')
        cur_date = datetime.now().strftime('%B %d, %Y')
        self.date_label.setText(cur_date)
        self.time_label.setText(cur_time)

    def updateclock(self, cur_time):
        ctime = cur_time.strftime('%H:%M:%S')
        self.time_label.setText(ctime)

    def sign_in(self):
        con = self.connection_check()
        if con is False:
            return 0
        checkpass = self.check_pass()
        if checkpass[0]:
            self.record_attendance('clock-in', checkpass[1])

    def sign_out(self):
        con = self.connection_check()
        if con is False:
            return 0
        checkpass = self.check_pass()
        if checkpass[0]:
            self.record_attendance('clock-out', checkpass[1])

    def log_request(self):
        con = self.connection_check()
        if con is False:
            return 0
        checkpass = self.check_pass()
        if checkpass[0]:
            self.show_logs('show my logs', checkpass[1])

    def all_log_request(self):
        con = self.connection_check()
        if con is False:
            return 0
        checkpass = self.check_pass()
        if checkpass[0]:
            self.show_logs('show all logs', checkpass[1])

    def check_pass(self):
        userpass = self.user_pass.text()
        if userpass == '':
            QtGui.QMessageBox.information(self, 'Note',
                                      'Enter your user password', None)
            return [False]
        else:
            return True, userpass

    # def flash_loading(self):
    #     self.name_label.setText('Loading Data, Please Wait . . .')
    #     self.setEnabled(False)

    # def void_loading(self):
    #     self.user_pass.clear()
    #     self.name_label.setText('')

    # def capture_thread(self):
    #     dataSetCreator.DataSetCreator(0, 1, 100, 'dataSetsample')
    #     cv2.destroyAllWindows()

    def register_window_show(self):
        con = self.connection_check()
        if con is False:
            return 0
        register_window = RegisterWindow(self)
        login = AuthenticationWindow(self)
        if not login.exec_():
            login.hide()
        else:
            register_window.show()

    def edit_config_show(self):
        con = self.connection_check()
        if con is False:
            return 0
        globalconfig_window = GlobalConfigWindow(self)
        login = AuthenticationWindow(self)
        if not login.exec_():
            login.hide()
        else:
            globalconfig_window.show()

    def employee_list_show(self):
        con = self.connection_check()
        if con is False:
            return 0
        db = EMS_db_model()
        emp_list = db.fetch_profile()
        employee_list_window = EmployeeListView(emp_list, self)
        login = AuthenticationWindow(self)
        if not login.exec_():
            login.hide()
        else:
            employee_list_window.show()

    def clocked_employee_show(self):
        con = self.connection_check()
        if con is False:
            return 0
        db = EMS_db_model()
        emp_list = db.fetch_profile()
        clocked_employee_window = ClockedEmployeeWindow(emp_list, self)
        clocked_employee_window.show()

    def graphopt_show(self):
        con = self.connection_check()
        if con is False:
            return 0
        graph_window = GraphOpt(self)
        login = AuthenticationWindow(self)
        if not login.exec_():
            login.hide()
        else:
            graph_window.show()

    def memo_show(self):
        con = self.connection_check()
        if con is False:
            return 0
        memo_window = MemoWindow(self)
        login = AuthenticationWindow(self)
        if not login.exec_():
            login.hide()
        else:
            memo_window.show()

    def help_show(self):
        help_me = HelpWindow(self)
        help_me.show()

    def connection_check(self):
        try:
            EMS_db_model()
        except:
            QtGui.QMessageBox.warning(self, 'Connection Failed',
                                            'Cannot connect to the server,\nCheck your internet connection.', None)
            return False


class AuthCDWindow(QtGui.QDialog, authenticatecd.Ui_Form):
    def __init__(self, parent=None):
        super(AuthCDWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.label.setText('Reading Data Sets.')
        self.show()
        self.time_cd = 3
        self.time_timer = QtCore.QTimer(self)
        self.time_timer.timeout.connect(self.check)
        self.time_timer.start(1000)


    def check(self):
        self.label.setText('Authenticating face in ...')
        self.label_cd.setText(str(self.time_cd))
        self.time_cd -= 1
        if self.time_cd < 0:
            self.time_timer.stop()
            self.accept()


class AuthenticationWindow(QtGui.QDialog, authentication_form.Ui_authentication_form):
    def __init__(self, parent=None):
        super(AuthenticationWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.btn_faceAuth.clicked.connect(self.check)
        self.setWindowIcon(QtGui.QIcon('icons/favicon.png'))
        self.btn_faceAuth.setShortcut('Return')
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()

    def check(self):
        try:
            EMS_db_model()
        except:
            QtGui.QMessageBox.warning(self, 'Connection Failed',
                                      'Cannot connect to the server,\nCheck your internet connection.', None)
            self.pass_txt.clear()
            return 0

        # testing
        # if self.pass_txt.text() == '123':
        #     self.accept()
        # else:
        #     pass

        # production
        db = EMS_db_model()
        user_pass = self.pass_txt.text()
        if db.master_verify(user_pass):
            self.accept()
            return 0
        if user_pass == '':
            QtGui.QMessageBox.warning(self, 'Note',
                                      'Password Field cannot be empty', None)
        else:
            authCD = AuthCDWindow(self)
            if not authCD.exec_():
                login.hide()
            else:
                self.setEnabled(False)
                cap = Identifier.Detect(0)
                id = cap.identify()
                cv2.destroyAllWindows()
                self.setEnabled(True)
                if id is False:
                    QtGui.QMessageBox.warning(self, 'Authentication Failed',
                                              'Incorrect password or you are\n not authorized for this action', None)
                    self.pass_txt.clear()
                    return 0
                if id is None:
                    return 0
                authenticate = db.admin_verify(id, user_pass)
                if authenticate == 'Hi Creator' or authenticate is True:
                    self.accept()
                else:
                    QtGui.QMessageBox.warning(self, 'Authentication Failed',
                                              'Incorrect password or you are\n not authorized for this action', None)
                    self.pass_txt.clear()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    login = AuthenticationWindow()
    if not login.exec_():
        sys.exit()

    main = MainWindow()
    sys.exit(app.exec_())
