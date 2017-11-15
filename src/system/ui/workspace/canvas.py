from configparser import ConfigParser

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit
from PyQt5.QtCore import QSize

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
        self.initWidth = int(int(config['WINDOW']['width'])*2/3)
        self.initHeight = int(int(config['WINDOW']['height'])*2/3)
        
    def InitCanvas(self):    
        vbox = QVBoxLayout(self)
        vbox.setContentsMargins(0, 0, 0, 0)
        canvasLog = QTextEdit('Canvas')
        vbox.addWidget(canvasLog)
        self.setLayout(vbox)

    def sizeHint(self):
        return QSize(self.initWidth, self.initHeight)