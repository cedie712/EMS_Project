from PyQt4 import QtGui, QtCore
import HelpView
from models import EMS_db_model
import webbrowser

class HelpWindow(QtGui.QMainWindow, HelpView.Ui_HelpWindow):
    def __init__(self, parent=None):
        super(HelpWindow, self).__init__(parent)
        self.setupUi(self)
        self.setupUi(self)
        fg = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())
        self.setFixedSize(self.size())
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.pushButton_reset_pass.setText('Forgot Password?')

        self.pushButton_reset_pass.clicked.connect(self.forgot_pass)

    def forgot_pass(self):
        db = EMS_db_model()
        forgot_pass_link = db.get_forgot_pass_link()
        webbrowser.open(forgot_pass_link)