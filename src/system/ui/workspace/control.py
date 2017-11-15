from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtCore import Qt

from src.system.ui.workspace.canvas import CanvasWidget
from src.system.ui.workspace.colorwheel import ColorWheelWidget
from src.system.ui.workspace.frame import FrameWidget

class DockControl(object):
    
    def __init__(self, parent):
        self.parent = parent
        self.InitDock()
    
    def InitDock(self):
        self.canvas = CanvasWidget(self.parent)
        self.colorwheel = ColorWheelWidget(self.parent)
        self.frame = FrameWidget(self.parent)
        
        self.dock = {}        
        # Top Components        
        self.dock['Canvas'] = Dock('Canvas', self.parent)
        self.dock['Canvas'].setObjectName('CanvasDock')        
        self.dock['Canvas'].setWidget(self.canvas)
        self.parent.addDockWidget(Qt.TopDockWidgetArea, self.dock['Canvas'])
        
        self.dock['ColorWheel'] = Dock('ColorWheel', self.parent)        
        self.dock['ColorWheel'].setObjectName('ColorWheelDock')
        self.dock['ColorWheel'].setWidget(self.colorwheel)
        self.parent.addDockWidget(Qt.TopDockWidgetArea, self.dock['ColorWheel'])
        
        # Bottom Components
        self.dock['Frame'] = Dock('Frame', self.parent)        
        self.dock['Frame'].setObjectName('FrameDock')
        self.dock['Frame'].setWidget(self.frame)
        self.parent.addDockWidget(Qt.BottomDockWidgetArea, self.dock['Frame'])

class Dock(QDockWidget):
    
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.name = name
        self.parent = parent
        self.initDeskDock()
    
    def initDeskDock(self):
        self.setWindowTitle(self.name)
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.setFeatures(QDockWidget.AllDockWidgetFeatures)
