from configparser import ConfigParser

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QSize

from src.system.util.path import RelativePath
from src.system.ui.workspace.canvas.base import Canvas

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
        self.margin = int(config['CANVAS']['margin'])
        self.spacing = int(config['CANVAS']['spacing'])
        
    def InitCanvas(self):
        self.canvas = Canvas(self.parent)
        
        vbox = QVBoxLayout()
        vbox.setSpacing(self.spacing)
        vbox.setContentsMargins(self.margin, self.margin,
                                self.margin, self.margin)
        vbox.addWidget(self.canvas)
        self.setLayout(vbox)

    def sizeHint(self):
        return QSize(self.windowWidth*self.widthRatio,
                     self.windowHeight*self.heightRatio)