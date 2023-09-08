'''
Add titles another things
'''

from PyQt6.QtWidgets import QApplication,QWidget
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200,700,400)
        self.setWindowTitle('Tuto4 Adds')
        self.setWindowIcon(QIcon('pocs/pyqt/tuto1/icon.jpg'))
        self.setFixedWidth(700)
        self.setFixedHeight(400)
        self.setStyleSheet('background-color:green')
        self.setWindowOpacity(0.5)
        
    


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())