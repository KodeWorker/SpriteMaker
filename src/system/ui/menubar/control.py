from src.system.ui.menubar.file import FileMenu
from src.system.ui.menubar.help import HelpMenu

class MenuBarControl(object):
    
    def __init__(self, parent):
        self.parent = parent
        self.InitMenuBar()
    
    def InitMenuBar(self):
        menuBar = self.parent.menuBar()
        
        fileMenu = menuBar.addMenu('&File')            
        FileMenu(fileMenu, self.parent)

        helpMenu = menuBar.addMenu('&Help')            
        HelpMenu(helpMenu, self.parent)