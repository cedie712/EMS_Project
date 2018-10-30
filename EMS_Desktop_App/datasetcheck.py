from PyQt4 import QtGui, QtCore
import recap
import cv2
from face import dataSetCreator
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class CaptureCheckWindow(QtGui.QDialog, recap.Ui_DataSetCapWin):
    def __init__(self, user_id, parent=None):
        super(CaptureCheckWindow, self).__init__(parent)
        self.setupUi(self)
        self.id = user_id

        self.sampleA.setPixmap(QtGui.QPixmap(_fromUtf8("dataSetsample/%s.0.jpg" % str(self.id))))
        self.sampleA.setScaledContents(True)
        self.sampleA.setObjectName(_fromUtf8("sampleA"))

        self.sampleB.setPixmap(QtGui.QPixmap(_fromUtf8("dataSetsample/%s.1.jpg" % str(self.id))))
        self.sampleB.setScaledContents(True)
        self.sampleB.setObjectName(_fromUtf8("sampleB"))

        self.pushButton_2.clicked.connect(self.check)
        self.pushButton.clicked.connect(self.recapture)
        self.show()

    def check(self):
        self.accept()

    def recapture(self):
        self.setEnabled(False)
        dataSetCreator.DataSetCreator(0, int(self.id), 1, 'dataSetsample')
        cv2.destroyAllWindows()

        self.sampleA.setPixmap(QtGui.QPixmap(_fromUtf8("dataSetsample/%s.0.jpg" % str(self.id))))
        self.sampleA.setScaledContents(True)
        self.sampleA.setObjectName(_fromUtf8("sampleA"))

        self.sampleB.setPixmap(QtGui.QPixmap(_fromUtf8("dataSetsample/%s.1.jpg" % str(self.id))))
        self.sampleB.setScaledContents(True)
        self.sampleB.setObjectName(_fromUtf8("sampleB"))

        self.setEnabled(True)