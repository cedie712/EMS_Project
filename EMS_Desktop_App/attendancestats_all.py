import sys
from PyQt4 import QtGui, QtCore
from models import EMS_db_model
from itertools import groupby
import numpy as np
from  scipy.interpolate import spline


from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from datetime import datetime

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s



class Tb(NavigationToolbar):
    toolitems = [t for t in NavigationToolbar.toolitems if
                 t[0] in ('Home', 'Pan', 'Zoom', 'Save')]


class AttendanceGraph(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AttendanceGraph, self).__init__(parent)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/favicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle('Employees\' Presence and Absence Average Count Comparison')

        fg = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())
        self.setMinimumSize(800, 500)

        logs = self.get_attendance_stat()
        if logs is not None:

            self.figure = Figure(figsize=(100, 600), facecolor='gray')
            self.canvas = FigureCanvas(self.figure)

            self.toolbar = Tb(self.canvas, self)

            graph = self.figure.add_subplot(111)

            graph.set_xlabel('Period', color='yellow')
            graph.set_ylabel('Count', color='yellow')

            x = np.array(logs['key'])
            y_presences = np.array(logs['attendance_ave'])
            y_absences = np.array(logs['absence_ave'])

            x_smooth = np.linspace(x.min(), x.max(), 300)
            y_presences_smooth = spline(x, y_presences, x_smooth)
            y_absences_smooth = spline(x, y_absences, x_smooth)

            # graph.plot(x, y_presences, linestyle=' ', marker='o', color='blue')
            # graph.plot(x_smooth, y_presences_smooth, label='average presence count', color='blue')

            # graph.plot(x, y_absences, linestyle=' ', marker='o', color='orange')
            # graph.plot(x_smooth, y_absences_smooth, label='average absence count', color='orange')

            graph.plot(x, y_presences, linestyle=' ', marker='o', color='blue')
            graph.plot(logs['key'], logs['attendance_ave'], label='average presence count', color='blue')

            graph.plot(x, y_absences, linestyle=' ', marker='o', color='orange')
            graph.plot(logs['key'], logs['absence_ave'], label='average absence count', color='orange')

            graph.grid(linestyle='-')
            graph.legend(loc='upper left')
            graph.ticklabel_format(useOffset=False)


            layout = QtGui.QVBoxLayout()
            layout.addWidget(self.toolbar)
            layout.addWidget(self.canvas)
            self.setLayout(layout)

            self.setWindowModality(QtCore.Qt.ApplicationModal)

    def get_attendance_stat(self):
        db = EMS_db_model()
        logs = db.get_salary_log()
        if len(logs) == 0:
            QtGui.QMessageBox.information(self, 'Note',
                                          'There are no attendance logs to plot', None)
            return None
        period = []
        attendances = []
        absences = []
        for k, v in groupby(logs, key=lambda x: x['period']):
            if k is None:
                continue
            vlistA = []
            vlistB = []
            splitter = k.split('/')
            whole_n_part = int(splitter[2].split(' ')[2])
            decimal_part = float(splitter[3] + splitter[4]) * 0.01 / 12
            k = float(whole_n_part + decimal_part)
            k = round(k, 2)
            for i in list(v):
                vlistA.append(i['days_present'])
                vlistB.append(i['days_absent'])
            vlistA = sum(vlistA) / len(vlistA)
            vlistB = sum(vlistB) / len(vlistB)
            period.append(k)
            attendances.append(vlistA)
            absences.append(vlistB)
        logs_dict = {
            'key': period,
            'attendance_ave': attendances,
            'absence_ave': absences
        }
        return logs_dict
