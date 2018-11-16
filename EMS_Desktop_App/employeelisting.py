from PyQt4 import QtGui, QtCore
import EmployeeList
import spfunc as sp
from Profile import ProfileWindow
from functools import partial

class EmployeeListView(QtGui.QMainWindow, EmployeeList.Ui_EmployeeList):
    def __init__(self, emp_list, parent=None):
        super(EmployeeListView, self).__init__(parent)
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
        active_count = 0
        inactive_count = 0
        for i in sorted(self.emp_list, key=lambda k: k['last_name'].lower()):
            btn_text = '  ' + sp.convert_id(i['id'], i['start_date'][:4]) \
                       + '   %s, %s %s' % \
                       (i['last_name'].capitalize(), i['first_name'].capitalize(), i['middle_name'].capitalize())
            btn_link = QtGui.QPushButton(btn_text, self.scrollArea)
            if i['is_active']:
                active_count += 1
                btn_link.setStyleSheet("text-align: left;\n color: #fff;\n"
                                       "background-color: rgb(0, 156, 5);")
            else:
                inactive_count += 1
                btn_link.setStyleSheet("text-align: left;\n color: #fff;\n"
                                       "background-color: rgb(209, 51, 51);")
            btn_link.clicked.connect(partial(self.grep_profile, i['id']))
            self.scrollLayout.addWidget(btn_link)
            self.scrollArea.setWidget(self.scrollContent)

        self.label_active.setText(str(active_count))
        self.label_inactive.setText(str(inactive_count))
        self.label_inactive.setStyleSheet("QLabel {color: orangered;}")


    def grep_profile(self, uid):
        profile_window = ProfileWindow(uid, self)
        profile_window.show()
