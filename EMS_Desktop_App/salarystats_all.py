import numpy as np
import sys
from PyQt4 import QtGui, QtCore
from models import EMS_db_model
from itertools import groupby

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class Tb(NavigationToolbar2QT):
    # only display the buttons we need
    toolitems = [t for t in NavigationToolbar2QT.toolitems if
                 t[0] in ('Home', 'Pan', 'Zoom', 'Save')]


class SalaryGraph(QtGui.QWidget):
    def __init__(self, parent=None):
        super(SalaryGraph, self).__init__(parent)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/favicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle('Employees\' Overall Average Salary through Pay Period')

        fg = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())
        self.setMinimumSize(800, 500)

        logs = self.get_salary_stat()
        if logs is not None:

            self.figure = Figure(figsize=(100, 600), facecolor='#f5faff')

            self.canvas = FigureCanvas(self.figure)

            self.toolbar = Tb(self.canvas, self)

            N = len(logs['salary_ave'])
            salary_ave = tuple(logs['salary_ave'])
            ind = np.arange(N) # the x locations for the groups
            width = 0.35  # the width of the bars: can also be len(x) sequence

            ax = self.figure.add_subplot(111)

            ax.bar(ind, salary_ave, width, color='orange')
            ax.set_ylabel('Salary in PHP', color='orangered')
            ax.set_xlabel('Period', color='orangered')
            ax.set_xticks(ind)
            ax.set_xticklabels(logs['key'])

            self.canvas.draw()

            layout = QtGui.QVBoxLayout()
            layout.addWidget(self.toolbar)
            layout.addWidget(self.canvas)
            self.setLayout(layout)
            self.setWindowModality(QtCore.Qt.ApplicationModal)



    def get_salary_stat(self):
        db = EMS_db_model()
        logs = db.get_salary_log()[::-1]
        if len(logs) == 0:
            QtGui.QMessageBox.information(self, 'Note',
                                          'There are no salary logs to plot', None)
            return None
        period = []
        salary = []
        for k, v in groupby(logs, key=lambda x: x['period']):
            if k is None:
                continue
            vlistA = []
            splitter = k.split('/')
            whole_n_part = int(splitter[2].split(' ')[2][2:])
            decimal_part = float(splitter[3] + splitter[4]) * 0.01 / 12
            k = float(whole_n_part + decimal_part)
            k = round(k, 2)
            for i in list(v):
                vlistA.append(i['net_pay'])
            vlistA = sum(vlistA) / len(vlistA)
            period.append(k)
            salary.append(vlistA)
        logs_dict = {
            'key': period,
            'salary_ave': salary,
        }
        return logs_dict
