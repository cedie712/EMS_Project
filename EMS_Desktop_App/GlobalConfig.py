from PyQt4 import QtGui, QtCore
import GlobalConfigView
from models import EMS_db_model


class GlobalConfigWindow(QtGui.QMainWindow, GlobalConfigView.Ui_UpdateConfigWindow):
    def __init__(self, parent=None):
        super(GlobalConfigWindow, self).__init__(parent)
        self.setupUi(self)
        fg = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())
        self.setFixedSize(self.size())
        self.update_btn.setDisabled(True)
        self.current_config = None
        self.get_current_config()

        pstart_text = "%sth day of month"
        pend_text = "%sth day of month"
        lvl_1_text = self.current_config['lvl_1_rate']
        lvl_2_text = self.current_config['lvl_2_rate']
        lvl_3_text = self.current_config['lvl_3_rate']
        ot_text = self.current_config['ot_rate']
        sss_pay_day = self.current_config['sss_pay_day']
        philhealth_pay_day = self.current_config['philhealth_pay_day']
        pagibig_pay_day = self.current_config['pagibig_pay_day']
        tax_pay_day = self.current_config['tax_pay_day']

        start_combo_content = [
            pstart_text % '5',
            pstart_text % '10',
            pstart_text % '15',
        ]

        end_combo_content = [
            pend_text % '20',
            pend_text % '25',
            pend_text % '30',
        ]

        cut_offs = ['second cut-off', 'first cut-off']

        for i in cut_offs:
            self.sss_pday.addItem(i)
            self.philhealth_pday.addItem(i)
            self.pagibig_pday.addItem(i)
            self.tax_pday.addItem(i)

        if pstart_text % sss_pay_day in start_combo_content:
            self.sss_pday.setCurrentIndex(1)

        if pstart_text % pagibig_pay_day in start_combo_content:
            self.pagibig_pday.setCurrentIndex(1)

        if pstart_text % philhealth_pay_day in start_combo_content:
            self.philhealth_pday.setCurrentIndex(1)

        if pstart_text % tax_pay_day in start_combo_content:
            self.tax_pday.setCurrentIndex(1)

        for i in start_combo_content:
            self.start_combo.addItem(i)

        for i in end_combo_content:
            self.end_combo.addItem(i)

        self.lvl_1_rate_edit.setValue(lvl_1_text)
        self.lvl_2_rate_edit.setValue(lvl_2_text)
        self.lvl_3_rate_edit.setValue(lvl_3_text)
        self.ot_rate_edit.setValue(ot_text)

        if self.current_config['pstart'] == 10:
            self.start_combo.setCurrentIndex(1)
            self.end_combo.setCurrentIndex(1)

        if self.current_config['pstart'] == 15:
            self.start_combo.setCurrentIndex(2)
            self.end_combo.setCurrentIndex(2)

        self.enable_radio.setChecked(True)
        if self.current_config['is_operating'] is False:
            self.disable_radio.setChecked(True)

        self.start_combo.currentIndexChanged.connect(self.enable_save_btn)
        self.end_combo.currentIndexChanged.connect(self.enable_save_btn)
        self.sss_pday.currentIndexChanged.connect(self.enable_save_btn)
        self.philhealth_pday.currentIndexChanged.connect(self.enable_save_btn)
        self.pagibig_pday.currentIndexChanged.connect(self.enable_save_btn)
        self.tax_pday.currentIndexChanged.connect(self.enable_save_btn)

        self.lvl_1_rate_edit.valueChanged.connect(self.enable_save_btn)
        self.lvl_2_rate_edit.valueChanged.connect(self.enable_save_btn)
        self.lvl_3_rate_edit.valueChanged.connect(self.enable_save_btn)
        self.ot_rate_edit.valueChanged.connect(self.enable_save_btn)

        self.start_combo.currentIndexChanged.connect(self.match_cut_off_start)
        self.end_combo.currentIndexChanged.connect(self.match_cut_off_end)
        self.update_btn.clicked.connect(self.save_changes)
        self.cancel_btn.clicked.connect(self.cancel)

        self.enable_radio.clicked.connect(self.enable_save_btn)
        self.disable_radio.clicked.connect(self.enable_save_btn)

        self.setWindowModality(QtCore.Qt.ApplicationModal)


    def get_current_config(self):
        db = EMS_db_model()
        current = db.get_config()[0]
        content = {
            'pstart': current['first_cutoff'],
            'pend': current['second_cutoff'],
            'lvl_1_rate': current['level_1_rate'],
            'lvl_2_rate': current['level_2_rate'],
            'lvl_3_rate': current['level_3_rate'],
            'ot_rate': current['overtime_rate'],
            'sss_pay_day' : current['sss_pay_day'],
            'philhealth_pay_day': current['philhealth_pay_day'],
            'pagibig_pay_day': current['pagibig_pay_day'],
            'tax_pay_day': current['tax_pay_day'],
            'is_operating': current['is_operating'],
        }

        self.current_config = content

    def match_cut_off_start(self):
        if self.start_combo.currentIndex() == 0:
            self.end_combo.setCurrentIndex(0)
        if self.start_combo.currentIndex() == 1:
            self.end_combo.setCurrentIndex(1)
        if self.start_combo.currentIndex() == 2:
            self.end_combo.setCurrentIndex(2)

    def match_cut_off_end(self):
        if self.end_combo.currentIndex() == 0:
            self.start_combo.setCurrentIndex(0)
        if self.end_combo.currentIndex() == 1:
            self.start_combo.setCurrentIndex(1)
        if self.end_combo.currentIndex() == 2:
            self.start_combo.setCurrentIndex(2)

    def save_changes(self):
        lvl1_rate = float(self.lvl_1_rate_edit.text()[4:])
        lvl2_rate = float(self.lvl_2_rate_edit.text()[4:])
        lvl3_rate = float(self.lvl_3_rate_edit.text()[4:])
        ot_rate = float(self.ot_rate_edit.text())

        is_operating = False
        if self.enable_radio.isChecked():
            is_operating = True

        if lvl1_rate >= lvl2_rate or lvl1_rate >= lvl3_rate\
                or lvl2_rate >= lvl3_rate:
            note = 'rates should vary. level 1 rate should have the lowest value.\n' \
                   ' level 2 rate should be greater than level 1 and level 3 should\n' \
                   ' be greater than level 2'
            QtGui.QMessageBox.information(self, 'Note', note, None)
            return 0

        first_cut_off = int(self.start_combo.currentText().replace("th day of month", ''))
        second_cut_off = int(self.end_combo.currentText().replace("th day of month", ''))

        sss_pday_new = second_cut_off
        if self.sss_pday.currentIndex() == 1:
            sss_pday_new = first_cut_off

        philhealth_pday_new = second_cut_off
        if self.philhealth_pday.currentIndex() == 1:
            philhealth_pday_new = first_cut_off

        pagibig_pday_new = second_cut_off
        if self.pagibig_pday.currentIndex() == 1:
            pagibig_pday_new = first_cut_off

        tax_pday_new = second_cut_off
        if self.tax_pday.currentIndex() == 1:
            tax_pday_new = first_cut_off

        if any(i < 50 for i in [lvl1_rate, lvl2_rate, lvl3_rate]):
            note = 'any of rates should not be less than PHP 50'
            QtGui.QMessageBox.information(self, 'Note', note, None)
            return 0

        if ot_rate < 1:
            note = 'overtime rate should not be less than 1'
            QtGui.QMessageBox.information(self, 'Note', note, None)
            return 0

        content = {
            "first_cutoff": first_cut_off,
            "second_cutoff": second_cut_off,
            "level_1_rate": lvl1_rate,
            "level_2_rate": lvl2_rate,
            "level_3_rate": lvl3_rate,
            "overtime_rate": ot_rate,
            "pagibig_pay_day": pagibig_pday_new,
            "philhealth_pay_day": philhealth_pday_new,
            "sss_pay_day": sss_pday_new,
            "tax_pay_day": tax_pday_new,
            "is_operating": is_operating
        }

        db = EMS_db_model()
        save = db.update_global_conf(content)
        if save == 'configurations are updated':
            QtGui.QMessageBox.information(self, 'Note', save, None)
            self.hide()
            self.update_btn.setDisabled(True)

    def enable_save_btn(self):
        self.update_btn.setDisabled(False)

    def cancel(self):
        self.update_btn.setDisabled(True)
        self.hide()
