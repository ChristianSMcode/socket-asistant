# Form implementation generated from reading ui file '.\pocs\pyqt\tuto2\radioButton\raido_w_group.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(301, 118)
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 20, 271, 76))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton.setObjectName("radioButton")
        #self.radioButton.toggled.connect(self.selected)
        
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.verticalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton_2.setObjectName("radioButton_2")
        #self.radioButton_2.toggled.connect(self.selected)
        self.buttonGroup.addButton(self.radioButton_2)
        self.buttonGroup.buttonClicked.connect(self.selected)
        self.verticalLayout_3.addWidget(self.radioButton_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.result_1 = QtWidgets.QLabel(parent=self.widget)
        self.result_1.setObjectName("result_1")
        self.horizontalLayout.addWidget(self.result_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton_3.setObjectName("radioButton_3")
        #self.radioButton_3.toggled.connect(self.selected2)
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_3)
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton_4.setObjectName("radioButton_4")
        #self.radioButton_4.toggled.connect(self.selected2)
        self.buttonGroup_2.addButton(self.radioButton_4)
        self.buttonGroup_2.buttonClicked.connect(self.selected2)
        self.verticalLayout.addWidget(self.radioButton_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
            
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def selected(self):
        print(self.buttonGroup.checkedButton().text())
        
    def selected2(self):
        print(self.buttonGroup_2.checkedButton().text())
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select1"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.radioButton.setText(_translate("Dialog", "A"))
        self.radioButton_2.setText(_translate("Dialog", "B"))
        self.label_2.setText(_translate("Dialog", "Select2"))
        self.result_1.setText(_translate("Dialog", "TextLabel"))
        self.radioButton_3.setText(_translate("Dialog", "C"))
        self.radioButton_4.setText(_translate("Dialog", "D"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
