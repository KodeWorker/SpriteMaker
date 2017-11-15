""" Sprite Maker
# Description:
    This is the main program of Sprite Maker.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/11/15
"""
import sys
from configparser import ConfigParser

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon

from src.system.util.path import RelativePath
from src.system.ui.menubar.manager import MenuBarManager
from src.system.ui.toolbar.manager import ToolBarManager
from src.system.ui.workspace.manager import WorkspaceManager
from src.system.action.menubar.control import MenuBarControl
from src.system.action.toolbar.control import ToolBarControl

class SpriteMaker(QMainWindow,
                  MenuBarControl,
                  ToolBarControl):
    """ Sprite Maker Class
        This class is the main window of the program.
    """
    
    def __init__(self):
        super().__init__()
        self.InitConfig()
        self.InitUI()
        
    def InitConfig(self):
        """ Initiate Configuration
            This method reads the values from config files.
        """
        
        config = ConfigParser()
        config.read(RelativePath('config', 'default.conf'))
        self.windowTitle = config['WINDOW']['title']
        self.windowWidth = int(config['WINDOW']['width'])
        self.windowHeight = int(config['WINDOW']['height'])
        
    def InitUI(self):
        """ Initiate User-Interface
            This method initiates the main window and its UI managers.
        """
        
        # Window initiation
        self.setWindowTitle(self.windowTitle)
        self.setWindowIcon(QIcon(RelativePath('asset',
                                              'image',
                                              'icon.png')))
        self.resize(self.windowWidth, self.windowHeight)
        center_point = QDesktopWidget().availableGeometry().center()
        self.frameGeometry().moveCenter(center_point)
        
        # UI manager
        MenuBarManager(self)
        ToolBarManager(self)
        WorkspaceManager(self)
        
        self.show()
    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    sm = SpriteMaker()
    sys.exit(app.exec_())
