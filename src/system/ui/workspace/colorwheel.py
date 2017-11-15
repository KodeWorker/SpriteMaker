from configparser import ConfigParser

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt, QSize

from src.system.util.path import RelativePath

class ColorWheelWidget(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.InitConfig()
        self.InitColorWheel()
    
    def InitConfig(self):
        config = ConfigParser()
        config.read(RelativePath('config', 'default.conf'))
        self.windowWidth = int(config['WINDOW']['width'])
        self.windowHeight = int(config['WINDOW']['height'])
        self.widthRatio = float(config['CANVAS']['widthRatio'])
        self.heightRatio = float(config['CANVAS']['heightRatio'])
        self.margin =int(config['COLORWHEEL']['margin'])
    
    def InitColorWheel(self):
        self.parent.colorWheel = ColorWheel(self.parent)
        
        vbox = QVBoxLayout()
        vbox.setContentsMargins(self.margin, self.margin,
                                self.margin, self.margin)
        vbox.addWidget(self.parent.colorWheel)
        self.setLayout(vbox)
    
    def sizeHint(self):
        return QSize(self.windowWidth*(1 - self.widthRatio),
                     self.windowHeight*(1 - self.heightRatio))
        
class ColorWheel(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.InitColorWheel()
    
    def InitColorWheel(self):
        qPalette = QPalette()
        qPalette.setColor(QPalette.Background, Qt.lightGray)
        self.setAutoFillBackground(True)
        self.setPalette(qPalette)
