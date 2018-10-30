# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/captureFace.ui'
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

class Ui_DataSetCapWin(object):
    def setupUi(self, DataSetCapWin):
        DataSetCapWin.setObjectName(_fromUtf8("DataSetCapWin"))
        DataSetCapWin.resize(436, 309)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/favicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DataSetCapWin.setWindowIcon(icon)
        self.pushButton = QtGui.QPushButton(DataSetCapWin)
        self.pushButton.setGeometry(QtCore.QRect(170, 260, 121, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/facerecoglogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.sampleB = QtGui.QLabel(DataSetCapWin)
        self.sampleB.setGeometry(QtCore.QRect(230, 60, 171, 181))
        self.sampleB.setText(_fromUtf8(""))
        self.sampleB.setPixmap(QtGui.QPixmap(_fromUtf8("icons/pic.png")))
        self.sampleB.setScaledContents(True)
        self.sampleB.setObjectName(_fromUtf8("sampleB"))
        self.pushButton_2 = QtGui.QPushButton(DataSetCapWin)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 260, 121, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Check-mark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.sampleA = QtGui.QLabel(DataSetCapWin)
        self.sampleA.setGeometry(QtCore.QRect(30, 60, 171, 181))
        self.sampleA.setText(_fromUtf8(""))
        self.sampleA.setPixmap(QtGui.QPixmap(_fromUtf8("icons/pic.png")))
        self.sampleA.setScaledContents(True)
        self.sampleA.setObjectName(_fromUtf8("sampleA"))
        self.label_3 = QtGui.QLabel(DataSetCapWin)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 371, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: orangered;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(DataSetCapWin)
        QtCore.QMetaObject.connectSlotsByName(DataSetCapWin)

    def retranslateUi(self, DataSetCapWin):
        DataSetCapWin.setWindowTitle(_translate("DataSetCapWin", "Face Data Set Capture", None))
        self.pushButton.setText(_translate("DataSetCapWin", "Re-Capture", None))
        self.pushButton_2.setText(_translate("DataSetCapWin", "ok, it\'s good", None))
        self.label_3.setText(_translate("DataSetCapWin", "I would like to know if you are contented\n"
"with these data set samples?", None))

