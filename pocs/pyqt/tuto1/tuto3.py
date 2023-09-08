'''
Use QDialog window, nuevamente con posibilidades
diferentes a Qwidget y mainwindow, por ejemplo este no se
puede maximizar ni minimizar
'''

from PyQt6.QtWidgets import QApplication,QDialog
import sys


app = QApplication(sys.argv)

window = QDialog()

window.show()
sys.exit(app.exec())