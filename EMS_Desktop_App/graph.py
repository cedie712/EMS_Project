from PyQt4 import QtGui, QtCore
import GraphsView
from busyboxgraph import BusyBoxWindow


class GraphOpt(QtGui.QMainWindow, GraphsView.Ui_ChartsWindow):
    def __init__(self, parent=None):
        super(GraphOpt, self).__init__(parent)
        self.setupUi(self)
        fg = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.toolButton_attendance.clicked.connect(self.show_attendance_graph)
        self.toolButton_salary.clicked.connect(self.show_salary_graph)

    def show_attendance_graph(self):
        BusyBoxWindow('attendance', self)

    def show_salary_graph(self):
        BusyBoxWindow('salary', self)
