from PyQt4 import QtGui, QtCore
import RegistrationWindow
from models import EMS_db_model
import cv2
from face import dataSetCreator
from datasetcheck import CaptureCheckWindow
import config


class RegisterWindow(QtGui.QMainWindow, RegistrationWindow.Ui_RegisterWindow):
    def __init__(self, parent=None):
        super(RegisterWindow, self).__init__(parent)
        self.setupUi(self)
        fg = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())
        self.setFixedSize(self.size())
        self.cancel_btn.clicked.connect(self.close_window)
        self.male_radio.setChecked(True)
        self.birthday_txt.setCalendarPopup(True)


        # regex
        regex_letter = QtCore.QRegExp("([a-zA-Z]+[ ])+")
        validator_letter = QtGui.QRegExpValidator(regex_letter)

        regex_nospace = QtCore.QRegExp("[a-zA-Z0-9_.-]+")
        validator_nospace = QtGui.QRegExpValidator(regex_nospace)

        regex_contact = QtCore.QRegExp("^9(?!(000000000))\d{9}$")
        validator_contact = QtGui.QRegExpValidator(regex_contact)

        regex_sss = QtCore.QRegExp("^(?!(0000))\d{4}-(?!0000000)\d{7}-(?!0000)\d{4}$")
        validator_sss = QtGui.QRegExpValidator(regex_sss)

        regex_philhealth = QtCore.QRegExp("^(?!(00))\d{2}-(?!(000000000))\d{9}-(?!(0))\d{1}$")
        validator_philhealth = QtGui.QRegExpValidator(regex_philhealth)

        regex_pagibig = QtCore.QRegExp("^(?!(0000))\d{4}-(?!(0000))\d{4}-(?!(0000))\d{4}$")
        validator_pagibig = QtGui.QRegExpValidator(regex_pagibig)

        regex_tin = QtCore.QRegExp("^(?!(000))\d{3}-(?!(000))\d{3}-(?!(000))\d{3}-(?!(00000))\d{5}$")
        validator_tin = QtGui.QRegExpValidator(regex_tin)

        regex_height = QtCore.QRegExp("^1(?!(00))\d{2}$")
        validator_height = QtGui.QRegExpValidator(regex_height)

        passEcho = QtGui.QLineEdit.Password

        self.username_txt.setValidator(validator_nospace)
        self.username_txt.setMaxLength(20)
        self.password_txt.setEchoMode(passEcho)
        self.password_txt.setMaxLength(25)
        self.confirm_txt.setEchoMode(passEcho)
        self.confirm_txt.setMaxLength(25)



        self.fname_txt.setValidator(validator_letter)
        self.fname_txt.setMaxLength(35)
        self.mname_txt.setValidator(validator_letter)
        self.mname_txt.setMaxLength(35)
        self.lname_txt.setValidator(validator_letter)
        self.lname_txt.setMaxLength(35)

        self.gmail_txt.setValidator(validator_nospace)
        self.gmail_txt.setMaxLength(30)

        self.height_txt.setValidator(validator_height)
        self.contact_txt.setValidator(validator_contact)
        self.sss_txt.setValidator(validator_sss)
        self.philhealth_txt.setValidator(validator_philhealth)
        self.pagibig_txt.setValidator(validator_pagibig)
        self.tin_txt.setValidator(validator_tin)

        # get config
        db = EMS_db_model()
        config = db.get_config()[0]

        # get rates
        rates_list = [config['level_1_rate'], config['level_2_rate'], config['level_3_rate']]
        for i in rates_list:
            self.rate_combo.addItem('PHP ' + str(i))

        position_lists = ['instructor', 'administrator']
        for i in position_lists:
            self.position_combo.addItem(i)

        self.train_btn.clicked.connect(self.register_user)

        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def register_user(self):
        db = EMS_db_model()
        position = str(self.position_combo.currentText())
        rate = float(self.rate_combo.currentText().split(' ')[1])
        dayoff = 'sunday'
        if self.checkBox_mon.isChecked():
            dayoff += ', monday'
        if self.checkBox_tue.isChecked():
            dayoff += ', tuesday'
        if self.checkBox_wed.isChecked():
            dayoff += ', wednesday'
        if self.checkBox_thu.isChecked():
            dayoff += ', thursday'
        if self.checkBox_fri.isChecked():
            dayoff += ', friday'
        if self.checkBox_sat.isChecked():
            dayoff += ', saturday'

        is_admin = False
        if position == 'administrator':
            is_admin = True

        gender = 'male'
        if self.female_radio.isChecked():
            gender = 'female'

        content = {
            'username': self.username_txt.text(),
            'password': self.password_txt.text(),
            'confirm': self.confirm_txt.text(),
            'email': self.gmail_txt.text(),
            'fname': self.fname_txt.text(),
            'mname': self.mname_txt.text(),
            'lname': self.lname_txt.text(),
            'position': position,
            'is_admin': is_admin,
            "sss_number": self.sss_txt.text(),
            "pagibig_number": self.pagibig_txt.text(),
            "philhealth_number": self.philhealth_txt.text(),
            "tin_number": self.tin_txt.text(),
            'rate': rate,
            'day_off': dayoff,
            'birthday': self.birthday_txt.text(),
            'address': self.address_txt.text(),
            'gender': gender,
            'height': self.height_txt.text(),
            'contact_number': self.contact_txt.text(),
        }

        title = 'Success'
        msg = 'Employee has been registered'

        dataCheck = [content['username'], content['password'], content['confirm'], content['email'], content['height'],
                     content['fname'], content['mname'], content['lname'], content['sss_number'],
                     content['contact_number'], content['philhealth_number'],
                     content['pagibig_number'], content['tin_number'], content['address']]

        for i in dataCheck:
            if len(str(i)) == 0 or i == None:
                title = 'Failed'
                msg = 'Complete the Fields'
                return QtGui.QMessageBox.information(self, title, msg, None)

        if len(dayoff.split(',')) > 4:
            title = 'Failed'
            msg = 'Maximum of 3 day-offs are allowed'
            return QtGui.QMessageBox.information(self, title, msg, None)


        if len(self.sss_txt.text()) != 17:
            title = 'Failed'
            msg = 'Incorrect SSS number'
        elif len(self.philhealth_txt.text()) != 14:
            title = 'Failed'
            msg = 'Incorrect PHILHEALTH number'
        elif len(self.pagibig_txt.text()) != 14:
            title = 'Failed'
            msg = 'Incorrect PAGIBIG number'
        elif len(self.tin_txt.text()) != 17:
            title = 'Failed'
            msg = 'Incorrect TIN number'
        else:
            register = db.register_user(content)

            if register == 'complete the fields':
                title = 'Failed'
                msg = register
            elif register == 'you are not yet at the proper age of working':
                title = 'Failed'
                msg = register
            elif register == 'passwords didn\'t match':
                title = 'Failed'
                msg = register
                self.password_txt.clear()
                self.confirm_txt.clear()
            #successful registration here
            elif register[0] is True:
                self.capture_dataset(register[1])
                check_if_ok = CaptureCheckWindow(register[1], self)
                if not check_if_ok.exec_():
                    check_if_ok.hide()
                    self.close_window()
                else:
                    self.close_window()
            else:
                title = 'Failed'
                msg = ''
                for i in register:
                    msg += i + '\n'
        QtGui.QMessageBox.information(self, title, msg, None)

    def capture_dataset(self, id):
        self.setEnabled(False)
        dataSetCreator.DataSetCreator(config.CAMERA_INDEX, id, 1, 'dataSetsample')
        cv2.destroyAllWindows()
        self.setEnabled(True)

    def close_window(self):
        self.tin_txt.clear()
        self.philhealth_txt.clear()
        self.sss_txt.clear()
        self.pagibig_txt.clear()
        self.username_txt.clear()
        self.password_txt.clear()
        self.confirm_txt.clear()
        self.fname_txt.clear()
        self.mname_txt.clear()
        self.lname_txt.clear()
        self.height_txt.clear()
        self.contact_txt.clear()
        self.address_txt.clear()
        self.gmail_txt.clear()
        self.close()
