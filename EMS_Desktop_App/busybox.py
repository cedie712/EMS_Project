from PyQt4 import QtGui, QtCore
import busyboxView


class BusyBoxWindow(QtGui.QDialog, busyboxView.Ui_busybox):
    def __init__(self, memo, img=None, parent=None):
        super(BusyBoxWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.memo = memo
        self.img = img
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()
        self.time_timer = QtCore.QTimer(self)
        self.time_timer.timeout.connect(self.fb_post)
        self.time_timer.start(1000)


    def fb_post(self):
        try:
            from facebookupload import FbUpload
            FbUpload(self.memo, self.img)
            self.time_timer.stop()
            self.hide()
            return QtGui.QMessageBox.information(self, 'Note',
                                                 'Memo has been posted.', None)
        except:
            self.time_timer.stop()
            self.hide()
            return QtGui.QMessageBox.information(self, 'Note',
                                                 'Memo post failed. It may be connection error, \n'
                                                 'improperly configured FB graph page id value or.\n'
                                                 ' invalid token. Try again.', None)

