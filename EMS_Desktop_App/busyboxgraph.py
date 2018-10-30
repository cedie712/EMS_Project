from PyQt4 import QtGui, QtCore
from salarystats_all import SalaryGraph
from attendancestats_all import AttendanceGraph
import busyboxView


class BusyBoxWindow(QtGui.QDialog, busyboxView.Ui_busybox):
    def __init__(self, graph, parent=None):
        super(BusyBoxWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.show()
        self.time_timer = QtCore.QTimer(self)
        if graph == 'salary':
            self.time_timer.timeout.connect(self.show_salary_graph)
        elif graph == 'attendance':
            self.time_timer.timeout.connect(self.show_attendance_graph)
        self.time_timer.start(1000)

        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def show_salary_graph(self):
        sal = SalaryGraph()
        sal.show()
        self.time_timer.stop()
        self.hide()

    def show_attendance_graph(self):
        att = AttendanceGraph()
        att.show()
        self.time_timer.stop()
        self.hide()
