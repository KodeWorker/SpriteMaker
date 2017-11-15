""" Menu Bar Manager
# Description:
    This script contains the higher-level manager of menu bar elements.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/11/15
"""

from src.system.ui.menubar.file import FileMenu
from src.system.ui.menubar.help import HelpMenu

class MenuBarManager(object):
    """ Menu Bar Manager Class    
        This class is the manager of menu bar elements.
        
        Parameters
        ----------
        parent: QMainWindow
            This is the main window of the program.
    """
    def __init__(self, parent):
        self.parent = parent
        self.InitMenuBar()
    
    def InitMenuBar(self):
        """ Initiate Menu Bar
            This method initiates all the elements in menu bar.
        """
        
        menuBar = self.parent.menuBar()
        
        fileMenu = menuBar.addMenu('&File')            
        FileMenu(fileMenu, self.parent)

        helpMenu = menuBar.addMenu('&Help')            
        HelpMenu(helpMenu, self.parent)