'''
Qlabel se usa para mostrar texto y/o imagenes y gifs
'''
import sys
from PyQt6.QtWidgets import QWidget,QApplication,QLabel
from PyQt6.QtGui import QIcon,QFont,QPixmap,QMovie #QMovie es para animaciones simples como gif sin sonido

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,700,400)
        self.setWindowTitle('QLabelTuto')
        self.setWindowIcon(QIcon('pocs/pyqt/tuto1/icon.jpg'))
        
        #label = QLabel('TestLabel',self)
        #label.setText('NewTestText')
        #label.move(100,100)
        #label.setFont(QFont("Sanserif",15))
        #label.setStyleSheet('color:blue')
        
        label = QLabel(self)
        label.setPixmap(QPixmap('pocs/pyqt/tuto1/icon.jpg'))

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())