# Form implementation generated from reading ui file '.\pocs\pyqt\tuto2\radioButton\radio.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(184, 142)
        Dialog.setStyleSheet("QLabel{\n"
"color:green\n"
"}")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_inse = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_inse.setFont(font)
        self.label_inse.setStyleSheet("Qlabel{\n"
"\n"
"color:green\n"
"}")
        self.label_inse.setObjectName("label_inse")
        self.verticalLayout_2.addWidget(self.label_inse)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(parent=Dialog)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(self.radio_selected)
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(parent=Dialog)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.radio_selected)
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(parent=Dialog)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.toggled.connect(self.radio_selected)
        self.verticalLayout.addWidget(self.radioButton_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.label_select = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_select.setFont(font)
        self.label_select.setText("")
        self.label_select.setObjectName("label_select")
        self.verticalLayout_3.addWidget(self.label_select)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def radio_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label_select.setText(radio_btn.text())   

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_inse.setText(_translate("Dialog", "Selected"))
        self.radioButton.setText(_translate("Dialog", "A"))
        self.radioButton_2.setText(_translate("Dialog", "B"))
        self.radioButton_3.setText(_translate("Dialog", "C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())