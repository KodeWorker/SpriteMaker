""" Help Menu Control
# Description:
    This script contains the user-interface controller of help menu in menu 
    bar.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/11/15
"""

from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

from src.system.util.path import RelativePath

class HelpMenu(object):
    """ File Menu Class
        This class is the controller of help menu elements.
        
        Parameters
        ----------
        menu: QMenu
            This is the added controlling menu in menu bar.            
        parent: QMainWindow
            This is the main window of the program.
    """
    
    def __init__(self, menu, parent):
        self.menu = menu
        self.parent = parent
        self.InitFileMenuElements()
        self.InitFileMenuLayout()
    
    def InitFileMenuElements(self):
        """ Initiate Help Menu Elements
            This method initiates all the help menu elements.
        """
        
        # MenuBar -> Help -> Report issue
        self.reportIssue = QAction(
                QIcon(RelativePath('asset',
                                   'image',
                                   'menubar',
                                   'help',
                                   'issue.png')),
                '&Report issue ...',
                self.parent)
        # No shortcut
        self.reportIssue.triggered.connect(self.parent.ReportIssue)
        # MenuBar -> Help -> About SpriteMaker
        self.aboutSpriteMaker = QAction(
                QIcon(RelativePath('asset',
                                   'image',
                                   'menubar',
                                   'help', 
                                   'info.png')),
                '&About SpriteMaker',
                self.parent)
        # No shortcut
        self.aboutSpriteMaker.triggered.connect(self.parent.AboutSpriteMaker)
        
    def InitFileMenuLayout(self):
        """ Initiate Help Menu Layout
            This method initiates the help menu layout.
        """
        
        self.menu.addAction(self.reportIssue)        
        self.menu.addSeparator()
        self.menu.addAction(self.aboutSpriteMaker)