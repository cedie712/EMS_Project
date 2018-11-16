# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/MemoWindow.ui'
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

class Ui_MemoWindow(object):
    def setupUi(self, MemoWindow):
        MemoWindow.setObjectName(_fromUtf8("MemoWindow"))
        MemoWindow.resize(544, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/favicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MemoWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MemoWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.upload_btn = QtGui.QPushButton(self.centralwidget)
        self.upload_btn.setGeometry(QtCore.QRect(300, 350, 111, 41))
        self.upload_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.upload_btn.setStyleSheet(_fromUtf8("color: #fff;\n"
"background-color: rgb(21, 141, 141);\n"
"font: 14px/20px \"Helvetica Neue\",Helvetica,Arial,sans-serif;"))
        self.upload_btn.setIconSize(QtCore.QSize(30, 30))
        self.upload_btn.setObjectName(_fromUtf8("upload_btn"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 81, 81))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/rem2.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.memo_text = QtGui.QPlainTextEdit(self.centralwidget)
        self.memo_text.setGeometry(QtCore.QRect(10, 100, 521, 201))
        self.memo_text.setObjectName(_fromUtf8("memo_text"))
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(250, 350, 51, 41))
        self.toolButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.toolButton.setStyleSheet(_fromUtf8("border: None;"))
        self.toolButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/fb_601351.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(40, 40))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.image_btn = QtGui.QToolButton(self.centralwidget)
        self.image_btn.setGeometry(QtCore.QRect(0, 300, 61, 51))
        self.image_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.image_btn.setStyleSheet(_fromUtf8("border: None;"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/pic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.image_btn.setIcon(icon2)
        self.image_btn.setIconSize(QtCore.QSize(50, 50))
        self.image_btn.setObjectName(_fromUtf8("image_btn"))
        self.image_text = QtGui.QLineEdit(self.centralwidget)
        self.image_text.setEnabled(False)
        self.image_text.setGeometry(QtCore.QRect(60, 310, 431, 33))
        self.image_text.setObjectName(_fromUtf8("image_text"))
        self.cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(420, 350, 111, 41))
        self.cancel_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_btn.setStyleSheet(_fromUtf8("font-size: 14px;\n"
"color: #fff;\n"
"background-color: rgb(229, 21, 21);\n"
""))
        self.cancel_btn.setIconSize(QtCore.QSize(30, 30))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.toolButton_clear = QtGui.QToolButton(self.centralwidget)
        self.toolButton_clear.setGeometry(QtCore.QRect(490, 300, 41, 51))
        self.toolButton_clear.setFocusPolicy(QtCore.Qt.NoFocus)
        self.toolButton_clear.setStyleSheet(_fromUtf8("border: None;"))
        self.toolButton_clear.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_clear.setIcon(icon3)
        self.toolButton_clear.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_clear.setObjectName(_fromUtf8("toolButton_clear"))
        MemoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MemoWindow)
        QtCore.QMetaObject.connectSlotsByName(MemoWindow)

    def retranslateUi(self, MemoWindow):
        MemoWindow.setWindowTitle(_translate("MemoWindow", "Post Memo", None))
        self.upload_btn.setText(_translate("MemoWindow", "Post", None))
        self.image_btn.setText(_translate("MemoWindow", "...", None))
        self.image_text.setPlaceholderText(_translate("MemoWindow", "Attach an Image", None))
        self.cancel_btn.setText(_translate("MemoWindow", "Cancel", None))

