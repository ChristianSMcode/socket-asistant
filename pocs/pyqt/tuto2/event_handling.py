'''
Manejo de eventos y slots (signals and slots)
evento-metodo (un slot es un metodo al que se conecta un evento(señal))

'''
import sys
from PyQt6.QtWidgets import QWidget,QApplication,QPushButton,QLabel,QHBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,700,400)
        self.setWindowTitle('signals and slots')
        
        self.create_widget()
        
    def create_widget(self):
        hbox = QHBoxLayout()
        btn = QPushButton('click')
        btn.clicked.connect(self.slot_clicked)
        self.label = QLabel('Default')
        hbox.addWidget(btn)
        hbox.addWidget(self.label)
        
        self.setLayout(hbox)

    def slot_clicked(self):
        self.label.setText('Custom')
        
app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())