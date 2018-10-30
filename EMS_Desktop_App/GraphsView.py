# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/GraphsView.ui'
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

class Ui_ChartsWindow(object):
    def setupUi(self, ChartsWindow):
        ChartsWindow.setObjectName(_fromUtf8("ChartsWindow"))
        ChartsWindow.resize(537, 275)
        ChartsWindow.setMinimumSize(QtCore.QSize(537, 275))
        ChartsWindow.setMaximumSize(QtCore.QSize(537, 275))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/favicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ChartsWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(ChartsWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.toolButton_attendance = QtGui.QToolButton(self.centralwidget)
        self.toolButton_attendance.setGeometry(QtCore.QRect(20, 10, 221, 221))
        self.toolButton_attendance.setFocusPolicy(QtCore.Qt.NoFocus)
        self.toolButton_attendance.setStyleSheet(_fromUtf8("QToolButton{border: None}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/function_graphic-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_attendance.setIcon(icon1)
        self.toolButton_attendance.setIconSize(QtCore.QSize(200, 200))
        self.toolButton_attendance.setObjectName(_fromUtf8("toolButton_attendance"))
        self.toolButton_salary = QtGui.QToolButton(self.centralwidget)
        self.toolButton_salary.setGeometry(QtCore.QRect(300, 10, 221, 221))
        self.toolButton_salary.setFocusPolicy(QtCore.Qt.NoFocus)
        self.toolButton_salary.setStyleSheet(_fromUtf8("QToolButton{border: None}"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/barbar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_salary.setIcon(icon2)
        self.toolButton_salary.setIconSize(QtCore.QSize(200, 200))
        self.toolButton_salary.setObjectName(_fromUtf8("toolButton_salary"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 220, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        ChartsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChartsWindow)
        QtCore.QMetaObject.connectSlotsByName(ChartsWindow)

    def retranslateUi(self, ChartsWindow):
        ChartsWindow.setWindowTitle(_translate("ChartsWindow", "Graphs", None))
        self.toolButton_attendance.setText(_translate("ChartsWindow", "...", None))
        self.toolButton_salary.setText(_translate("ChartsWindow", "...", None))
        self.label.setText(_translate("ChartsWindow", "Attendance ", None))
        self.label_2.setText(_translate("ChartsWindow", "Salary", None))

