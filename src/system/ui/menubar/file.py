from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

from src.system.util.path import RelativePath

class FileMenu(object):
    
    def __init__(self, menu, parent):
        self.menu = menu
        self.parent = parent
        self.InitFileMenuAction()
        self.ComposeFileMenuAction()
    
    def InitFileMenuAction(self):
        self.newAct = QAction(
                QIcon(RelativePath('asset',
                                   'image',
                                   'menubar',
                                   'file',
                                   'new.png')),
                '&New',
                self.parent)
        self.newAct.setShortcut('Ctrl+N')
        self.newAct.triggered.connect(self.parent.NewAct)
        
        self.openAct = QAction(
                QIcon(RelativePath('asset',
                                   'image',
                                   'menubar',
                                   'file',
                                   'open.png')),
                '&Open ...',
                self.parent)
        self.openAct.setShortcut('Ctrl+O')
        self.openAct.triggered.connect(self.parent.OpenAct)
        
        self.saveAct = QAction(
                QIcon(RelativePath('asset',
                                   'image',
                                   'menubar',
                                   'file',
                                   'save.png')),
                '&Save',
                self.parent)
        self.saveAct.setShortcut('Ctrl+S')
        self.saveAct.triggered.connect(self.parent.SaveAct)
        
        self.saveAllAct = QAction('&Save all', self.parent)
        self.saveAllAct.setShortcut('Ctrl+Alt+S')
        self.saveAllAct.triggered.connect(self.parent.SaveAllAct)
        
        self.saveAsAct = QAction('&Save as ...', self.parent)
        self.saveAsAct.setShortcut('Ctrl+Shift+S')
        self.saveAsAct.triggered.connect(self.parent.SaveAsAct)
        
        self.closeAct = QAction(
                QIcon(RelativePath('asset',
                                   'image',
                                   'menubar',
                                   'file', 
                                   'close.png')),
                '&Close',
                self.parent)
        # No shortcut
        self.closeAct.triggered.connect(self.parent.CloseAct)
        
        self.closeAllAct = QAction('&Close all', self.parent)
        self.closeAllAct.setShortcut('Ctrl+Shift+W')
        self.closeAllAct.triggered.connect(self.parent.CloseAllAct)
        
        self.quitAct = QAction(
                QIcon(RelativePath('asset', 
                                   'image',
                                   'menubar',
                                   'file',
                                   'quit.png')),
                '&Quit',
                self.parent)
        self.quitAct.setShortcut('Ctrl+Q')
        self.quitAct.triggered.connect(self.parent.QuitAct)
        
    def ComposeFileMenuAction(self):
        self.menu.addAction(self.newAct)
        self.menu.addSeparator()
        self.menu.addAction(self.openAct)
        self.menu.addSeparator()
        self.menu.addAction(self.saveAct)
        self.menu.addAction(self.saveAllAct)
        self.menu.addAction(self.saveAsAct)
        self.menu.addSeparator()
        self.menu.addAction(self.closeAct)
        self.menu.addAction(self.closeAllAct)
        self.menu.addSeparator()
        self.menu.addAction(self.quitAct)

