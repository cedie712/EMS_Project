# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/busybox.ui'
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

class Ui_busybox(object):
    def setupUi(self, busybox):
        busybox.setObjectName(_fromUtf8("busybox"))
        busybox.resize(413, 105)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/favicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        busybox.setWindowIcon(icon)
        self.frame = QtGui.QFrame(busybox)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 431, 121))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 40, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 81, 81))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("icons/timer.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(busybox)
        QtCore.QMetaObject.connectSlotsByName(busybox)

    def retranslateUi(self, busybox):
        busybox.setWindowTitle(_translate("busybox", "Wait", None))
        self.label.setText(_translate("busybox", "Requesting to the Server . . . ", None))

