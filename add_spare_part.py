# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_spare_part.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtWidgets import QMessageBox, QWidget

from sql import Ital_Session, SparePart, Machine, get_machines_id
from PyQt5 import QtCore, QtGui, QtWidgets
from sqlalchemy.orm.exc import MultipleResultsFound


class Ui_add_spare_part_QWidget(object):
    def setupUi(self, add_spare_part_QWidget):
        add_spare_part_QWidget.setObjectName("add_spare_part_QWidget")
        add_spare_part_QWidget.resize(330, 350)
        self.gridLayout = QtWidgets.QGridLayout(add_spare_part_QWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.machine_label = QtWidgets.QLabel(add_spare_part_QWidget)
        self.machine_label.setStyleSheet("font: 10pt;")
        self.machine_label.setObjectName("machine_label")
        self.gridLayout.addWidget(self.machine_label, 0, 0, 1, 1)
        self.machine_comboBox = QtWidgets.QComboBox(add_spare_part_QWidget)
        self.machine_comboBox.setStyleSheet("font: 10pt;")
        self.machine_comboBox.setObjectName("machine_comboBox")
        self.machine_comboBox.addItems(get_machines_id())
        self.gridLayout.addWidget(self.machine_comboBox, 0, 1, 1, 1)
        self.part_nr_label = QtWidgets.QLabel(add_spare_part_QWidget)
        self.part_nr_label.setStyleSheet("font: 10pt ;")
        self.part_nr_label.setObjectName("part_nr_label")
        self.gridLayout.addWidget(self.part_nr_label, 1, 0, 1, 1)
        self.part_nr_lineEdit = QtWidgets.QLineEdit(add_spare_part_QWidget)
        self.part_nr_lineEdit.setStyleSheet("font: 10pt;")
        self.part_nr_lineEdit.setObjectName("part_nr_lineEdit")
        self.gridLayout.addWidget(self.part_nr_lineEdit, 1, 1, 1, 1)
        self.description_label = QtWidgets.QLabel(add_spare_part_QWidget)
        self.description_label.setStyleSheet("font: 10pt ;")
        self.description_label.setObjectName("description_label")
        self.gridLayout.addWidget(self.description_label, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(add_spare_part_QWidget)
        self.textEdit.setStyleSheet("font: 10pt;")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 1, 1, 1)
        self.ml_code_label = QtWidgets.QLabel(add_spare_part_QWidget)
        self.ml_code_label.setStyleSheet("font: 10pt ;")
        self.ml_code_label.setObjectName("ml_code_label")
        self.gridLayout.addWidget(self.ml_code_label, 3, 0, 1, 1)
        self.ml_code_lineEdit = QtWidgets.QLineEdit(add_spare_part_QWidget)
        self.ml_code_lineEdit.setStyleSheet("font: 10pt ;")
        self.ml_code_lineEdit.setObjectName("ml_code_lineEdit")
        self.gridLayout.addWidget(self.ml_code_lineEdit, 3, 1, 1, 1)
        self.ital_code_label = QtWidgets.QLabel(add_spare_part_QWidget)
        self.ital_code_label.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0, 0, 255);\n")
        self.ital_code_label.setObjectName("ital_code_label")
        self.gridLayout.addWidget(self.ital_code_label, 4, 0, 1, 1)
        self.ital_code_lineEdit = QtWidgets.QLineEdit(add_spare_part_QWidget)
        self.ital_code_lineEdit.setStyleSheet("font: 10pt;")
        self.ital_code_lineEdit.setObjectName("ital_code_lineEdit")
        self.gridLayout.addWidget(self.ital_code_lineEdit, 4, 1, 1, 1)
        self.ital_price_label = QtWidgets.QLabel(add_spare_part_QWidget)
        self.ital_price_label.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0, 0, 255);\n")
        self.ital_price_label.setObjectName("ital_price_label")
        self.gridLayout.addWidget(self.ital_price_label, 5, 0, 1, 1)
        self.ital_price_lineEdit = QtWidgets.QLineEdit(add_spare_part_QWidget)
        self.ital_price_lineEdit.setStyleSheet("font: 10pt ;")
        self.ital_price_lineEdit.setText("")
        self.ital_price_lineEdit.setObjectName("ital_price_lineEdit")
        self.gridLayout.addWidget(self.ital_price_lineEdit, 5, 1, 1, 1)
        self.info_code_label = QtWidgets.QLabel(add_spare_part_QWidget)
        self.info_code_label.setStyleSheet("background-color: rgb(170, 255, 0); color: rgb(15, 15, 15);")
        self.info_code_label.setObjectName("info_code_label")
        self.gridLayout.addWidget(self.info_code_label, 6, 0, 1, 1)
        self.info_code_lineEdit = QtWidgets.QLineEdit(add_spare_part_QWidget)
        self.info_code_lineEdit.setStyleSheet("font: 10pt; ")
        self.info_code_lineEdit.setText("")
        self.info_code_lineEdit.setObjectName("info_code_lineEdit")
        self.gridLayout.addWidget(self.info_code_lineEdit, 6, 1, 1, 1)
        self.info_site_code_label = QtWidgets.QLabel(add_spare_part_QWidget)
        self.info_site_code_label.setStyleSheet("background-color: rgb(170, 255, 0); color: rgb(15, 15, 15);")
        self.info_site_code_label.setObjectName("info_site_code_label")
        self.gridLayout.addWidget(self.info_site_code_label, 7, 0, 1, 1)
        self.info_site_code_lineEdit = QtWidgets.QLineEdit(add_spare_part_QWidget)
        self.info_site_code_lineEdit.setStyleSheet("font: 10pt;")
        self.info_site_code_lineEdit.setText("")
        self.info_site_code_lineEdit.setObjectName("info_site_code_lineEdit")
        self.gridLayout.addWidget(self.info_site_code_lineEdit, 7, 1, 1, 1)
        self.info_price_label = QtWidgets.QLabel(add_spare_part_QWidget)
        self.info_price_label.setStyleSheet("background-color: rgb(170, 255, 0); color: rgb(15, 15, 15);")
        self.info_price_label.setObjectName("info_price_label")
        self.gridLayout.addWidget(self.info_price_label, 8, 0, 1, 1)
        self.info_price_lineEdit = QtWidgets.QLineEdit(add_spare_part_QWidget)
        self.info_price_lineEdit.setStyleSheet("font: 10pt;")
        self.info_price_lineEdit.setText("")
        self.info_price_lineEdit.setObjectName("info_price_lineEdit")
        self.gridLayout.addWidget(self.info_price_lineEdit, 8, 1, 1, 1)
        self.save_btn = QtWidgets.QPushButton(add_spare_part_QWidget)
        self.save_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.save_btn.setStyleSheet("background-color: rgb(0, 170, 0); color: rgb(255, 255, 255); font: 10pt;")
        self.save_btn.setObjectName("save_btn")
        self.save_btn.clicked.connect(lambda: self.add_spare_part())
        self.gridLayout.addWidget(self.save_btn, 9, 1, 1, 2)

        self.retranslateUi(add_spare_part_QWidget)
        QtCore.QMetaObject.connectSlotsByName(add_spare_part_QWidget)

    def retranslateUi(self, add_spare_part_QWidget):
        _translate = QtCore.QCoreApplication.translate
        add_spare_part_QWidget.setWindowTitle(_translate("add_spare_part_QWidget", "Προσθήκη προϊόντος"))
        self.machine_label.setText(_translate("add_spare_part_QWidget", "Μηχάνημα"))
        self.part_nr_label.setText(_translate("add_spare_part_QWidget", "Part No"))
        self.description_label.setText(_translate("add_spare_part_QWidget", "Περιγραφή"))
        self.ml_code_label.setText(_translate("add_spare_part_QWidget", "Κωδικός"))
        self.ital_code_label.setText(_translate("add_spare_part_QWidget", "Ιταλία Κωδικός"))
        self.ital_price_label.setText(_translate("add_spare_part_QWidget", "Ιταλία Τιμή"))
        self.info_code_label.setText(_translate("add_spare_part_QWidget", "Info Κωδικός"))
        self.info_site_code_label.setText(_translate("add_spare_part_QWidget", "Info Site Κωδικός"))
        self.info_price_label.setText(_translate("add_spare_part_QWidget", "Info Τιμή"))
        self.save_btn.setText(_translate("add_spare_part_QWidget", "Αποθήκευση"))

    def add_spare_part(self):
        machine = self.machine_comboBox.currentText()
        try:
            machine_obj = Ital_Session.query(Machine).filter(Machine.model == machine).one_or_none()
            part_nr = self.part_nr_lineEdit.text()
            description = self.textEdit.toPlainText()
            ml_code = self.ml_code_lineEdit.text()
            ital_price = self.ital_price_lineEdit.text().replace(",", ".") + " €"
            ital_code = self.ital_code_lineEdit.text()
            info_code = self.info_code_lineEdit.text()
            info_site_code = self.info_site_code_lineEdit.text()
            info_price = self.info_price_lineEdit.text().replace(",", ".") + " €"
            new_spare_part = SparePart(machine=machine_obj.ID, part_nr=part_nr, description=description, ml_code=ml_code,
                                       ital_code=ital_code, ital_price=ital_price, info_code=info_code,
                                       info_site_code=info_site_code, info_price=info_price)
        except MultipleResultsFound:
            msgBox = QMessageBox.critical(None, "Σφάλμα", f"Βρέθηκαν πολλά {machine}")
            return

        Ital_Session.add(new_spare_part)
        Ital_Session.commit()
        msgBox = QMessageBox.information(None, "Πληροφορία", f"Το προιόν αποθηκεύτηκε!")
        return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet("QPushButton {max-height: 40px; min-width: 300px;"
                      "border-top-right-radius: 20px; border-bottom-left-radius: 20px; background-color: #ff9800;}"
                      "QPushButton:enabled { background-color: #55aa7f; color: white; }")
    add_spare_part_QWidget = QtWidgets.QWidget()
    ui = Ui_add_spare_part_QWidget()
    ui.setupUi(add_spare_part_QWidget)
    add_spare_part_QWidget.show()
    sys.exit(app.exec_())
