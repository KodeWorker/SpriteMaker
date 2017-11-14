from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtCore import Qt

from src.system.ui.dock.canvas import CanvasWidget
from src.system.ui.dock.colorwheel import ColorWheelWidget
from src.system.ui.dock.frame import FrameWidget

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
        self.parent.addDockWidget(Qt.TopDockWidgetArea, self.dock['Canvas'])
        self.dock['Canvas'].setWidget(self.canvas)
        
        self.dock['ColorWheel'] = Dock('ColorWheel', self.parent)
        self.parent.addDockWidget(Qt.TopDockWidgetArea, self.dock['ColorWheel'])
        self.dock['ColorWheel'].setObjectName('ColorWheelDock')
        self.dock['ColorWheel'].setWidget(self.colorwheel)
        
        # Bottom Components
        self.dock['Frame'] = Dock('Frame', self.parent)
        self.parent.addDockWidget(Qt.BottomDockWidgetArea, self.dock['Frame'])
        self.dock['Frame'].setObjectName('FrameDock')
        self.dock['Frame'].setWidget(self.frame)
        
        # Fixed DockWidget Size
#        self.dock['ColorWheel'].setMinimumWidth(300)
#        self.dock['ColorWheel'].setMaximumWidth(300)
#        self.dock['Frame'].setMinimumHeight(150)
#        self.dock['Frame'].setMaximumHeight(150)
        
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
