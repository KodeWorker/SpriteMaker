""" Workspace Manager
# Description:
    This script contains the higher-level manager of workspace elements.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/11/15
"""

from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtCore import Qt

from src.system.ui.workspace.canvas.manager import CanvasWidget
from src.system.ui.workspace.colorwheel.manager import ColorWheelWidget
from src.system.ui.workspace.frame.manager import FrameWidget

class WorkspaceManager(object):
    """ Workspace Manager Class
        This class is the manager of workspace elements
        
        Parameters
        ----------
        parent: QMainWindow
            This is the main window of the program.
    """
    
    def __init__(self, parent):
        self.parent = parent
        self.InitWorkspace()
    
    def InitWorkspace(self):
        """ Initiate Workspace
            This method initiates all the elements and its docking properties
            in workspace.
        """
        
        # Initiate elements
        self.parent.canvasWidget = CanvasWidget(self.parent)
        self.parent.colorwheelWidget = ColorWheelWidget(self.parent)
        self.parent.frameWidget = FrameWidget(self.parent)
        
        # Set docking properties
        self.dock = {}        
        # Top Components        
        self.dock['Canvas'] = TopButtomDock('Canvas', self.parent)        
        self.dock['Canvas'].setWidget(self.parent.canvasWidget)
        self.parent.addDockWidget(Qt.TopDockWidgetArea, self.dock['Canvas'])
        
        self.dock['ColorWheel'] = TopButtomDock('ColorWheel', self.parent)
        self.dock['ColorWheel'].setWidget(self.parent.colorwheelWidget)
        self.parent.addDockWidget(Qt.TopDockWidgetArea, self.dock['ColorWheel'])
        
        # Bottom Components
        self.dock['Frame'] = TopButtomDock('Frame', self.parent)
        self.dock['Frame'].setWidget(self.parent.frameWidget)
        self.parent.addDockWidget(Qt.BottomDockWidgetArea, self.dock['Frame'])

class TopButtomDock(QDockWidget):
    """ Dock Class
        This class is QDockWidget with corresponding name of workspaces.
        
        Parameters
        ----------
        name: str
            This is the name of the workspace.
        parent: QMainWindow
            This is the main window of the program.
    """
    
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.name = name
        self.parent = parent
        self.InitDock()
    
    def InitDock(self):
        """ Initiate Dock
            This method initiates docking properies.
        """
        
        self.setWindowTitle(self.name)
        self.setObjectName(self.name)
        self.setAllowedAreas(Qt.TopDockWidgetArea | Qt.BottomDockWidgetArea)
        self.setFeatures(QDockWidget.AllDockWidgetFeatures)
