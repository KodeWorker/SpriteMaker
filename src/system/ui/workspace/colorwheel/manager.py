from configparser import ConfigParser

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QSize

from src.system.util.path import RelativePath
from src.system.ui.workspace.colorwheel.base import ColorWheel

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
        self.margin = int(config['COLORWHEEL']['margin'])
        self.spacing = int(config['COLORWHEEL']['spacing'])
        
    def InitColorWheel(self):
        self.colorWheel = ColorWheel(self.parent)
        
        vbox = QVBoxLayout()
        vbox.setSpacing(self.spacing)
        vbox.setContentsMargins(self.margin, self.margin,
                                self.margin, self.margin)
        vbox.addWidget(self.colorWheel)
        self.setLayout(vbox)
    
    def sizeHint(self):
        return QSize(self.windowWidth*(1 - self.widthRatio),
                     self.windowHeight*(1 - self.heightRatio))