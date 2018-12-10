from PyQt4 import QtGui, QtCore
import authenticatecd

class AuthCDWindow(QtGui.QDialog, authenticatecd.Ui_Form):
    def __init__(self, parent=None):
        super(AuthCDWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.label.setText('Reading Data Sets.')
        self.show()
        self.time_cd = 3
        self.time_timer = QtCore.QTimer(self)
        self.time_timer.timeout.connect(self.check)
        self.time_timer.start(1000)


    def check(self):
        self.label.setText('  Identifying face in ...')
        self.label_cd.setText(str(self.time_cd))
        self.time_cd -= 1
        if self.time_cd < 0:
            self.time_timer.stop()
            self.accept()
