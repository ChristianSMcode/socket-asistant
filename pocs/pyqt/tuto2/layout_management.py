'''
QHBOX layout is used to align the widgets horizontally
H=Horizontal
-Se puede añadir espaciamiento
-Se puede apeñuscar el layout (stretch)

QVBOX layout is used to align the widgets vertically
V=Vertical
-Se puede añadir espaciamiento
-Se puede apeñuscar el layout (stretch)

QGrid permite usar columnas y filas para organizar elementos

'''
import sys
from PyQt6.QtWidgets import QWidget,QApplication,QHBoxLayout,QPushButton,QVBoxLayout,QGridLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,700,400)
        self.setWindowTitle('Qhbox layout')
        
        btn1 = QPushButton('Click one')
        btn2 = QPushButton('Click two')
        btn3 = QPushButton('Click three')
        btn4 = QPushButton('Click four')
        
        h_layout = QHBoxLayout()
        
        h_layout.addWidget(btn1)
        h_layout.addWidget(btn2)

        
        #self.setLayout(h_layout)
        
        v_layout = QVBoxLayout()
        
        v_layout.addWidget(btn3)
        v_layout.addWidget(btn4)
  
        
        #self.setLayout(v_layout)
        
        g_layout = QGridLayout()
        
        g_layout.addWidget(btn1,0,0)
        g_layout.addWidget(btn2,0,1)
        
        g_layout.addWidget(btn3,1,0)
        g_layout.addWidget(btn4,1,1)
      
        self.setLayout(g_layout)
        
app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())