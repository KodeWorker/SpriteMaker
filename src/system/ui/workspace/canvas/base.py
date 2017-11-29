""" Canvas Widget
# Description:
    This script contains all elements in Canvas Widgets.
# Author: Shin-Fu (Kelvin) Wu <fxp61005@gmail.com>
# Date: 2017/11/29
"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt

class Canvas(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.InitCanvas()
    
    def InitCanvas(self):
        
        qPalette = QPalette()
        qPalette.setColor(QPalette.Background, Qt.lightGray)
        self.setAutoFillBackground(True)
        self.setPalette(qPalette)