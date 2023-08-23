import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from dotenv import load_dotenv

load_dotenv(dotenv_path='pocs/pyqt/.qt.env')

class MyWindow(QMainWindow):
    def __init__(self,xpos,ypos,width,height):
        super(MyWindow,self).__init__()
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.setGeometry(self.xpos,self.ypos,self.width,self.height)
        self.setWindowTitle('PyQT POC')
        self.initUi()
    
    def initUi(self):
        # (Add test label)
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Hello PyQt')
        self.label.move(50,50)
        
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me")
        self.b1.clicked.connect(self.clicked)
    
    def clicked(self):
        self.label.setText('Button pressed')      

def window():
    xpos  = int(os.getenv('XPOS') if os.getenv('XPOS') != None else 201)
    ypos  = int(os.getenv('YPOS') if os.getenv('YPOS') != None else 201)
    width = int(os.getenv('WIDTH') if os.getenv('WIDTH') != None else 301)
    height= int(os.getenv('HEIGHT') if os.getenv('HEIGHT') != None else 301)
    
    app = QApplication(sys.argv)
    win = MyWindow(xpos,ypos,width,height)   
    win.show()
    
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    window()
    
    
    
