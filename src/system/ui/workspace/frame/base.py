from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt

class TimeLine(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.InitTimeLine()
    
    def InitTimeLine(self):
        qPalette = QPalette()
        qPalette.setColor(QPalette.Background, Qt.lightGray)
        self.setAutoFillBackground(True)
        self.setPalette(qPalette)