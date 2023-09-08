'''
Use QMainWindow window
Aqui se puede acceder a otros elementos como StatusBar
QtoolBat etc, elementos que no serían accecibles usange
QWidget window
'''
from PyQt6.QtWidgets import QApplication,QMainWindow
import sys


app = QApplication(sys.argv)

window = QMainWindow()
window.statusBar().showMessage('PyQt6 course')

window.show()
sys.exit(app.exec())
