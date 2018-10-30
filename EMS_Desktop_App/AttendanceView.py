# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/AttendanceWindow.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AttendanceWindow(object):
    def setupUi(self, AttendanceWindow):
        AttendanceWindow.setObjectName(_fromUtf8("AttendanceWindow"))
        AttendanceWindow.resize(500, 515)
        AttendanceWindow.setMinimumSize(QtCore.QSize(500, 515))
        AttendanceWindow.setMaximumSize(QtCore.QSize(500, 515))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/favicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AttendanceWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(AttendanceWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.attendance_table = QtGui.QTableWidget(self.centralwidget)
        self.attendance_table.setGeometry(QtCore.QRect(10, 100, 481, 401))
        self.attendance_table.setObjectName(_fromUtf8("attendance_table"))
        self.attendance_table.setColumnCount(0)
        self.attendance_table.setRowCount(0)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 10, 91, 81))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/678120-calendar-clock-512.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.search_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.search_lineEdit.setGeometry(QtCore.QRect(10, 50, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.search_lineEdit.setFont(font)
        self.search_lineEdit.setText(_fromUtf8(""))
        self.search_lineEdit.setObjectName(_fromUtf8("search_lineEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 50, 31, 31))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("icons/search (1).png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        AttendanceWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AttendanceWindow)
        QtCore.QMetaObject.connectSlotsByName(AttendanceWindow)

    def retranslateUi(self, AttendanceWindow):
        AttendanceWindow.setWindowTitle(_translate("AttendanceWindow", "Attendance History", None))

