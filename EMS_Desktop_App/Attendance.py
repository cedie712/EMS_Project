from PyQt4 import QtGui, QtCore
from models import EMS_db_model
import AttendanceView
import spfunc as sp
from dateutil.parser import parse
import pytz
time_zone = pytz.timezone('Asia/Manila')


class AttendanceWindow(QtGui.QMainWindow, AttendanceView.Ui_AttendanceWindow):
    def __init__(self, attendance_logs, parent=None):
        super(AttendanceWindow, self).__init__(parent)
        self.setupUi(self)
        fg = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())
        self.setFixedSize(self.size())
        self.statusBar().setVisible(False)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.logs = attendance_logs

        self.attendance_table.setColumnCount(2)
        self.attendance_table.setRowCount(len(self.logs))
        self.attendance_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.attendance_table_headers = ['Time-In', 'Time-Out']
        self.attendance_table.setHorizontalHeaderLabels(self.attendance_table_headers)
        self.header = self.attendance_table.horizontalHeader()
        self.header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.header.setResizeMode(1, QtGui.QHeaderView.Stretch)

        self.filtering_list = []
        self.search_lineEdit.textChanged.connect(self.filter)

        row = 0
        for i in self.logs:
            time_in = parse(i['time_in']).astimezone(time_zone)
            time_in = time_in.strftime("%B %d, %Y %I:%M:%S %p")
            time_out = ' '
            if i['time_out'] is not None:
                time_out = parse(i['time_out']).astimezone(time_zone)
                time_out = time_out.strftime("%B %d, %Y %I:%M:%S %p")
            self.attendance_table.setItem(row, 0, QtGui.QTableWidgetItem(str(time_in)))
            self.attendance_table.setItem(row, 1, QtGui.QTableWidgetItem(str(time_out)))
            row += 1
            self.filtering_list.append([time_in, time_out])
        self.attendance_table.scrollToBottom()


    def filter(self):
        filter_string = self.search_lineEdit.text().lower()
        new_logs = []

        for i in self.filtering_list:
            if filter_string in i[0].lower() or filter_string in i[1]:
                new_logs.append(i)
        row = 0
        self.attendance_table.setRowCount(len(new_logs))
        for i in new_logs:
            self.attendance_table.setItem(row, 0, QtGui.QTableWidgetItem(i[0]))
            self.attendance_table.setItem(row, 1, QtGui.QTableWidgetItem(i[1]))
            row += 1
        self.attendance_table.scrollToBottom()
