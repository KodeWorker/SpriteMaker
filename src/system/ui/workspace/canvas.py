from configparser import ConfigParser

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt, QSize

from src.system.util.path import RelativePath

class CanvasWidget(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.InitConfig()
        self.InitCanvas()
        
    def InitConfig(self):
        config = ConfigParser()
        config.read(RelativePath('config', 'default.conf'))
        self.windowWidth = int(config['WINDOW']['width'])
        self.windowHeight = int(config['WINDOW']['height'])
        self.widthRatio = float(config['CANVAS']['widthRatio'])
        self.heightRatio = float(config['CANVAS']['heightRatio'])
        self.margin = float(config['CANVAS']['margin'])
        
    def InitCanvas(self):
        
        self.parent.canvas = Canvas(self.parent)
        vbox = QVBoxLayout()
        vbox.setContentsMargins(self.margin, self.margin,
                                self.margin, self.margin)
        vbox.addWidget(self.parent.canvas)
        self.setLayout(vbox)

    def sizeHint(self):
        return QSize(self.windowWidth*self.widthRatio,
                     self.windowHeight*self.heightRatio)

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