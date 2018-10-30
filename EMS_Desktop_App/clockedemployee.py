from PyQt4 import QtGui, QtCore
import ClockedinView
from functools import partial
from Profile import ProfileWindow
import spfunc as sp


class ClockedEmployeeWindow(QtGui.QMainWindow, ClockedinView.Ui_ClockedEmployee):
    def __init__(self, emp_list, parent=None):
        super(ClockedEmployeeWindow, self).__init__(parent)
        self.setupUi(self)
        fg = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())
        self.setFixedSize(self.size())

        self.scrollArea.setWidgetResizable(True)
        self.scrollContent = QtGui.QWidget(self.scrollArea)
        self.scrollLayout = QtGui.QVBoxLayout(self.scrollContent)
        self.scrollLayout.setAlignment(QtCore.Qt.AlignTop)
        self.scrollContent.setLayout(self.scrollLayout)

        self.emp_list = emp_list
        self.get_employee_list()
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def convert_id(self, idx, yr):
        return 'GCC' + str(idx) + '-' + str(yr)[2:]

    def get_employee_list(self):
        for i in self.emp_list[::-1]:
            if i['is_clocked_in']:
                btn_text = '  ' + sp.convert_id(i['id'], i['start_date'][:4]) \
                           + '   %s, %s %s' % (i['last_name'], i['first_name'], i['middle_name'])
                btn_link = QtGui.QPushButton(btn_text, self.scrollArea)
                btn_link.setStyleSheet("QPushButton { text-align: left; }")
                btn_link.clicked.connect(partial(self.grep_profile, i['id']))
                self.scrollLayout.addWidget(btn_link)
                self.scrollArea.setWidget(self.scrollContent)

    def grep_profile(self, uid):
        from controller import AuthenticationWindow
        profile_window = ProfileWindow(uid, self)
        login = AuthenticationWindow(self)
        if not login.exec_():
            login.hide()
        else:
            profile_window.show()