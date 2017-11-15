from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

from src.system.util.path import RelativePath

class HelpMenu(object):
    
    def __init__(self, menu, parent):
        self.menu = menu
        self.parent = parent
        self.InitFileMenuAction()
        self.ComposeFileMenuAction()
    
    def InitFileMenuAction(self):
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
        
    def ComposeFileMenuAction(self):
        self.menu.addAction(self.reportIssue)        
        self.menu.addSeparator()
        self.menu.addAction(self.aboutSpriteMaker)