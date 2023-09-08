'''
Use Qwidget window
Diferente en posibilidades con QMainWindow, como
semanticamente se indica un MainWindow es principal y un 
widget cumple otras funciones
'''
from PyQt6.QtWidgets import QApplication,QWidget
import sys


app = QApplication(sys.argv)

window = QWidget()

window.show()
sys.exit(app.exec())
