# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/EmployeeList.ui'
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

class Ui_EmployeeList(object):
    def setupUi(self, EmployeeList):
        EmployeeList.setObjectName(_fromUtf8("EmployeeList"))
        EmployeeList.resize(400, 496)
        EmployeeList.setMinimumSize(QtCore.QSize(400, 496))
        EmployeeList.setMaximumSize(QtCore.QSize(400, 496))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/favicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EmployeeList.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(EmployeeList)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 90, 381, 371))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 367))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 71, 71))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/profilexxx.png")))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 470, 61, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 470, 81, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_active = QtGui.QLabel(self.centralwidget)
        self.label_active.setGeometry(QtCore.QRect(80, 470, 81, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_active.setFont(font)
        self.label_active.setStyleSheet(_fromUtf8("color: green;"))
        self.label_active.setText(_fromUtf8(""))
        self.label_active.setObjectName(_fromUtf8("label_active"))
        self.label_inactive = QtGui.QLabel(self.centralwidget)
        self.label_inactive.setGeometry(QtCore.QRect(240, 470, 111, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_inactive.setFont(font)
        self.label_inactive.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.label_inactive.setText(_fromUtf8(""))
        self.label_inactive.setObjectName(_fromUtf8("label_inactive"))
        EmployeeList.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmployeeList)
        QtCore.QMetaObject.connectSlotsByName(EmployeeList)

    def retranslateUi(self, EmployeeList):
        EmployeeList.setWindowTitle(_translate("EmployeeList", "Employee List", None))
        self.label_2.setText(_translate("EmployeeList", "Active: ", None))
        self.label_3.setText(_translate("EmployeeList", "Inactive: ", None))

