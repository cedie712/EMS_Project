import MemoView
from PyQt4 import QtGui, QtCore
from busybox import BusyBoxWindow

class MemoWindow(QtGui.QMainWindow, MemoView.Ui_MemoWindow):
    def __init__(self, parent=None):
        super(MemoWindow, self).__init__(parent)
        self.setupUi(self)
        fg = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())
        self.setFixedSize(self.size())

        self.image_btn.clicked.connect(self.show_file_dialog)
        self.upload_btn.clicked.connect(self.post)

        self.cancel_btn.clicked.connect(self.cancel)

        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def post(self):
        img = None
        memo = self.memo_text.toPlainText()
        if len(memo) == 0:
            return QtGui.QMessageBox.information(self, 'Note',
                                                'Put a message or desciption or whatever you call it', None)

        if len(self.image_text.text()) != 0:
            img = self.image_text.text()
        BusyBoxWindow(memo, img, self)


    def show_file_dialog(self):
        dlg = QtGui.QFileDialog()
        dlg.setFileMode(QtGui.QFileDialog.AnyFile)
        dlg.setFilter("Image files (*.jpeg *.jpg *.png)")

        if dlg.exec_():
            filename = dlg.selectedFiles()[0]
            self.image_text.setText(filename)


    def cancel(self):
        self.memo_text.clear()
        self.image_text.setText("Attach an Image")
        self.hide()
