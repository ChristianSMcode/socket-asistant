# Form implementation generated from reading ui file '.\pocs\pyqt\tuto2\calculator\calculator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 184)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(12, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.firstLineEdit = QtWidgets.QLineEdit(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.firstLineEdit.setFont(font)
        self.firstLineEdit.setObjectName("firstLineEdit")
        self.horizontalLayout.addWidget(self.firstLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.SecondLineEdit = QtWidgets.QLineEdit(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SecondLineEdit.setFont(font)
        self.SecondLineEdit.setObjectName("SecondLineEdit")
        self.horizontalLayout_2.addWidget(self.SecondLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Add = QtWidgets.QPushButton(parent=Form)
        self.Add.setObjectName("Add")
        self.Add.clicked.connect(self.add)
        self.horizontalLayout_3.addWidget(self.Add)
        self.Sustract = QtWidgets.QPushButton(parent=Form)
        self.Sustract.setObjectName("Sustract")
        self.Sustract.clicked.connect(self.sustract)
        self.horizontalLayout_3.addWidget(self.Sustract)
        self.multiply = QtWidgets.QPushButton(parent=Form)
        self.multiply.setObjectName("multiply")
        self.multiply.clicked.connect(self.multiply_func)
        self.horizontalLayout_3.addWidget(self.multiply)
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.divide)
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.firstLineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.firstLineEdit_2.setFont(font)
        self.firstLineEdit_2.setPlaceholderText("")
        self.firstLineEdit_2.setObjectName("firstLineEdit_2")
        self.horizontalLayout_4.addWidget(self.firstLineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def add(self):
        fnum = int(self.firstLineEdit.text())
        snum = int(self.SecondLineEdit.text())
        self.firstLineEdit_2.setText(str(fnum + snum))
         
    def sustract(self):
        fnum = int(self.firstLineEdit.text())
        snum = int(self.SecondLineEdit.text())
        self.firstLineEdit_2.setText(str(fnum - snum))
        
    def multiply_func(self):
        fnum = int(self.firstLineEdit.text())
        snum = int(self.SecondLineEdit.text())
        self.firstLineEdit_2.setText(str(fnum * snum))
        
    def divide(self):
        fnum = int(self.firstLineEdit.text())
        snum = int(self.SecondLineEdit.text())
        self.firstLineEdit_2.setText(str(fnum / snum))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "First Number"))
        self.firstLineEdit.setPlaceholderText(_translate("Form", "Please enter a number"))
        self.label_2.setText(_translate("Form", "Second Number"))
        self.SecondLineEdit.setPlaceholderText(_translate("Form", "Please enter a number"))
        self.Add.setText(_translate("Form", "+"))
        self.Sustract.setText(_translate("Form", "-"))
        self.multiply.setText(_translate("Form", "*"))
        self.pushButton_4.setText(_translate("Form", "/"))
        self.label_3.setText(_translate("Form", "Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
