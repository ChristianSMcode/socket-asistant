'''
Aqui se incluye  una muestra del resto de los widgets ya que en general todos usan el mismo tipo de logica, los metodos y funcionalidades interesantes que tengan se pondrán en comentarios para ser investigados en el momento que se necesite. 
'''

import sys
from PyQt6.QtWidgets import QWidget,QApplication,QRadioButton,QHBoxLayout,QLabel,QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,200,200)
        self.setWindowTitle('QGeneral widgets tuto')

        #QRadioButton
        self.label = QLabel('Hello')
        
        self.create_radio()
        
        
        
        
    def radio_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label.setText(radio_btn.text())   
       
        
    def create_radio(self):
        h_box = QHBoxLayout()
        r_button1 = QRadioButton('a',self)
        r_button2 = QRadioButton('b',self)
        r_button3 = QRadioButton('c',self)
        
        r_button1.toggled.connect(self.radio_selected)
        r_button2.toggled.connect(self.radio_selected)
        r_button3.toggled.connect(self.radio_selected)
        
        h_box.addWidget(r_button1)
        h_box.addWidget(r_button2)
        h_box.addWidget(r_button3)
        
        v_box = QVBoxLayout(self)
        v_box.addWidget(self.label)
        v_box.addLayout(h_box)
        
        self.setLayout(v_box)
            
        
        
app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())