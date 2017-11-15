import sys
from configparser import ConfigParser

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon

from src.system.util.path import RelativePath
from src.system.ui.menubar.control import MenuBarControl
from src.system.ui.toolbar.control import ToolBarControl
from src.system.ui.workspace.control import DockControl
from src.system.action.menubar.manager import MenuManager
from src.system.action.toolbar.tool import ToolManager

class SpriteMaker(QMainWindow,
                  MenuManager,
                  ToolManager):
    
    def __init__(self):
        super().__init__()
        self.InitConfig()
        self.InitUI()
        
    def InitConfig(self):
        config = ConfigParser()
        config.read(RelativePath('config', 'default.conf'))
        self.windowTitle = config['WINDOW']['title']
        self.windowWidth = int(config['WINDOW']['width'])
        self.windowHeight = int(config['WINDOW']['height'])
        
    def InitUI(self):        
        self.setWindowTitle(self.windowTitle)
        self.setWindowIcon(QIcon(RelativePath('asset',
                                              'image',
                                              'icon.png')))
        self.resize(self.windowWidth, self.windowHeight)
        center_point = QDesktopWidget().availableGeometry().center()
        self.frameGeometry().moveCenter(center_point)
        
        MenuBarControl(self)
        ToolBarControl(self)
        DockControl(self)
        
        self.show()
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ip = SpriteMaker()
    sys.exit(app.exec_())
