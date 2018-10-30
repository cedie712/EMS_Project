# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/authentication_form.ui'
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

class Ui_authentication_form(object):
    def setupUi(self, authentication_form):
        authentication_form.setObjectName(_fromUtf8("authentication_form"))
        authentication_form.setWindowModality(QtCore.Qt.NonModal)
        authentication_form.resize(490, 222)
        authentication_form.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label = QtGui.QLabel(authentication_form)
        self.label.setGeometry(QtCore.QRect(310, 190, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.btn_faceAuth = QtGui.QToolButton(authentication_form)
        self.btn_faceAuth.setGeometry(QtCore.QRect(300, 20, 171, 161))
        self.btn_faceAuth.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_faceAuth.setStyleSheet(_fromUtf8("QToolButton{border: None;}"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/facerecoglogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_faceAuth.setIcon(icon)
        self.btn_faceAuth.setIconSize(QtCore.QSize(200, 200))
        self.btn_faceAuth.setObjectName(_fromUtf8("btn_faceAuth"))
        self.pass_txt = QtGui.QLineEdit(authentication_form)
        self.pass_txt.setGeometry(QtCore.QRect(20, 90, 211, 33))
        self.pass_txt.setInputMask(_fromUtf8(""))
        self.pass_txt.setEchoMode(QtGui.QLineEdit.Password)
        self.pass_txt.setObjectName(_fromUtf8("pass_txt"))
        self.label_12 = QtGui.QLabel(authentication_form)
        self.label_12.setGeometry(QtCore.QRect(230, 80, 61, 51))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("icons/forgot-password-icon-9.png")))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_2 = QtGui.QLabel(authentication_form)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(authentication_form)
        QtCore.QMetaObject.connectSlotsByName(authentication_form)
        authentication_form.setTabOrder(self.pass_txt, self.btn_faceAuth)

    def retranslateUi(self, authentication_form):
        authentication_form.setWindowTitle(_translate("authentication_form", "Super User Authentication", None))
        self.label.setText(_translate("authentication_form", " Face Authentication", None))
        self.btn_faceAuth.setText(_translate("authentication_form", "...", None))
        self.pass_txt.setPlaceholderText(_translate("authentication_form", "Password", None))
        self.label_2.setText(_translate("authentication_form", "Password:", None))

