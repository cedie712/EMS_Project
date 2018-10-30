# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/ClockedIn_Employee.ui'
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

class Ui_ClockedEmployee(object):
    def setupUi(self, ClockedEmployee):
        ClockedEmployee.setObjectName(_fromUtf8("ClockedEmployee"))
        ClockedEmployee.resize(400, 496)
        ClockedEmployee.setMinimumSize(QtCore.QSize(400, 496))
        ClockedEmployee.setMaximumSize(QtCore.QSize(400, 496))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/favicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ClockedEmployee.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(ClockedEmployee)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 90, 381, 381))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 377))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 71, 71))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/user_valid-512.png")))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        ClockedEmployee.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(ClockedEmployee)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        ClockedEmployee.setStatusBar(self.statusBar)

        self.retranslateUi(ClockedEmployee)
        QtCore.QMetaObject.connectSlotsByName(ClockedEmployee)

    def retranslateUi(self, ClockedEmployee):
        ClockedEmployee.setWindowTitle(_translate("ClockedEmployee", "Clocked-In Employee List", None))

