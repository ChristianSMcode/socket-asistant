'''
QLine permite insertar y editar texto incluye drop drag undo redo etc
'''
import sys
from PyQt6.QtWidgets import QWidget,QApplication,QLineEdit

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,700,400)
        self.setWindowTitle('QLineEdit tuto')

        line_edit = QLineEdit(self)
        



app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())