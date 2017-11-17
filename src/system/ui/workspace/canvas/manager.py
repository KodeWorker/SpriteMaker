""" Canvas Widget Management
# Description:
    This script is the manager of elements in Canvas Widgets.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/11/16
"""

from configparser import ConfigParser

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QSize

from src.system.util.path import RelativePath
from src.system.ui.workspace.canvas.base import Canvas
from src.system.action.workspace.canvas.control import CanvasControl 

class CanvasManager(QWidget, CanvasControl):
    """ Canvas Manager Class
        This class controls the layout of canvas widget.
        
        Parameters
        ----------
        parent: QMainWindow
            This is the main window of the program.
    """
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.InitConfig()
        self.InitCanvasManager()
        
    def InitConfig(self):
        """ Initiate Configuration
            This method reads the values from config files.
        """
        config = ConfigParser()
        config.read(RelativePath('config', 'default.conf'))
        self.windowWidth = int(config['WINDOW']['width'])
        self.windowHeight = int(config['WINDOW']['height'])
        self.widthRatio = float(config['CANVAS']['widthRatio'])
        self.heightRatio = float(config['CANVAS']['heightRatio'])
        self.margin = int(config['CANVAS']['margin'])
        self.spacing = int(config['CANVAS']['spacing'])
        
    def InitCanvasManager(self):
        """ Initiate Canvas Handler
            This method initiates the canvas layout in the canvas widget.
        """
        self.canvas = Canvas(self.parent)
        
        vbox = QVBoxLayout()
        vbox.setSpacing(self.spacing)
        vbox.setContentsMargins(self.margin, self.margin,
                                self.margin, self.margin)
        vbox.addWidget(self.canvas)
        self.setLayout(vbox)

    def sizeHint(self):
        """ sizeHint
            This method is override for initializing size.
        """
        return QSize(self.windowWidth*self.widthRatio,
                     self.windowHeight*self.heightRatio)