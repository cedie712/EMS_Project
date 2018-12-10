from PyQt4 import QtGui, QtCore
import recap
import cv2
from face import dataSetCreator, Identifier
from flashCD import AuthCDWindow
import config
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class CaptureCheckWindow(QtGui.QDialog, recap.Ui_DataSetCapWin):
    def __init__(self, user_id, for_update=False, parent=None):
        super(CaptureCheckWindow, self).__init__(parent)
        self.setupUi(self)
        self.id = user_id
        self.for_update = for_update

        self.sampleA.setPixmap(QtGui.QPixmap(_fromUtf8("dataSetsample/%s.0.jpg" % str(self.id))))
        self.sampleA.setScaledContents(True)
        self.sampleA.setObjectName(_fromUtf8("sampleA"))

        self.sampleB.setPixmap(QtGui.QPixmap(_fromUtf8("dataSetsample/%s.1.jpg" % str(self.id))))
        self.sampleB.setScaledContents(True)
        self.sampleB.setObjectName(_fromUtf8("sampleB"))

        self.pushButton_2.clicked.connect(self.check)
        self.pushButton.clicked.connect(self.recapture)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()

    def check(self):
        self.accept()

    def recapture(self):
        authCD = AuthCDWindow(self)
        if not authCD.exec_():
            authCD.hide()
        else:
            if self.for_update:
                self.setEnabled(False)
                cap = Identifier.Detect(config.CAMERA_INDEX)
                id = cap.identify()
                cv2.destroyAllWindows()
                self.setEnabled(True)
                if id is False or int(id) == int(self.id):
                    self.setEnabled(False)
                    dataSetCreator.DataSetCreator(config.CAMERA_INDEX, int(self.id), 1, 'dataSetsample')
                    cv2.destroyAllWindows()
                else:
                    return QtGui.QMessageBox.warning(self, 'Note', 'That face was already in use by other users', None)
            else:
                self.setEnabled(False)
                cap = Identifier.Detect(config.CAMERA_INDEX)
                id = cap.identify()
                cv2.destroyAllWindows()
                self.setEnabled(True)
                if id is not False:
                    return QtGui.QMessageBox.warning(self, 'Note', 'That face was already in use.', None)
                self.setEnabled(False)
                dataSetCreator.DataSetCreator(config.CAMERA_INDEX, int(self.id), 1, 'dataSetsample')
                cv2.destroyAllWindows()


        self.sampleA.setPixmap(QtGui.QPixmap(_fromUtf8("dataSetsample/%s.0.jpg" % str(self.id))))
        self.sampleA.setScaledContents(True)
        self.sampleA.setObjectName(_fromUtf8("sampleA"))

        self.sampleB.setPixmap(QtGui.QPixmap(_fromUtf8("dataSetsample/%s.1.jpg" % str(self.id))))
        self.sampleB.setScaledContents(True)
        self.sampleB.setObjectName(_fromUtf8("sampleB"))

        self.setEnabled(True)
