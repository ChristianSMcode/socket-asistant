'''
Qlabel se usa para mostrar texto y/o imagenes y gifs
'''
import sys
from PyQt6.QtWidgets import QWidget,QApplication,QPushButton,QMenu
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,700,400)
        self.setWindowTitle('QLabelTuto')

        self.create_button()

        
    def create_button(self):
        testButton = QPushButton('Click',self)
        testButton.setIcon(QIcon('pocs/pyqt/tuto1/icon.jpg'))
        testButton.setIconSize(QSize(36,36))
        
        menu = QMenu()
        menu.addAction('Paste')
        testButton.setMenu(menu)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())