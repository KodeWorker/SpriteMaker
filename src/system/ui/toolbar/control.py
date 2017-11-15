from configparser import ConfigParser

from PyQt5.QtWidgets import QAction, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from src.system.util.path import RelativePath

class ToolBarControl(object):
    
    def __init__(self, parent):
        self.parent = parent
        self.InitConfig()
        self.InitToolBarAction()
        self.ComposeToolBarAction()
    
    def InitConfig(self):
        self.toolbar = QToolBar('Paint Tool')
        self.toolbar.setObjectName('PaintTool')
        
        config = ConfigParser()
        config.read(RelativePath('config', 'default.conf'))        
        if config['TOOLBAR']['alignment'] == 'left':
            self.parent.addToolBar(Qt.LeftToolBarArea , self.toolbar)
        elif config['TOOLBAR']['alignment'] == 'right':
            self.parent.addToolBar(Qt.RightToolBarArea , self.toolbar)
        elif config['TOOLBAR']['alignment'] == 'top':
            self.parent.addToolBar(Qt.TopToolBarArea , self.toolbar)
        elif config['TOOLBAR']['alignment'] == 'bottom':
            self.parent.addToolBar(Qt.BottmToolBarArea , self.toolbar)
        else:
            raise ValueError('Error: No such tool bar area!')
    
    def InitToolBarAction(self):
        # ToolBar -> Cursor
        self.cursorTool = QAction(
                QIcon(RelativePath('asset',
                                   'image',
                                   'toolbar',
                                   'cursor.png')),
                'cursor',
                self.parent)
        self.cursorTool.triggered.connect(self.parent.CursorTool)
        # ToolBar -> Pen
        self.penTool = QAction(
                QIcon(RelativePath('asset',
                                   'image',
                                   'toolbar',
                                   'pen.png')),
                'Pen',
                self.parent)
        self.penTool.triggered.connect(self.parent.PenTool)
        # ToolBar -> Eraser
        self.eraserTool = QAction(
                QIcon(RelativePath('asset',
                                   'image',
                                   'toolbar',
                                   'eraser.png')),
                'Eraser',
                self.parent)
        self.eraserTool.triggered.connect(self.parent.EraserTool)
        # ToolBar -> Line
        self.lineTool = QAction(
                QIcon(RelativePath('asset',
                                   'image',
                                   'toolbar',
                                   'line.png')), 
                'Line', 
                self.parent)
        self.lineTool.triggered.connect(self.parent.LineTool)
        # ToolBar -> Paint Bucket
        self.paintBucketTool = QAction(
                QIcon(RelativePath('asset',
                                   'image',
                                   'toolbar',
                                   'paint_bucket.png')),
                'Paint Bucket',
                self.parent)
        self.paintBucketTool.triggered.connect(self.parent.PaintBucketTool)
        
    def ComposeToolBarAction(self):
        self.toolbar.addAction(self.cursorTool)
        self.toolbar.addAction(self.penTool)
        self.toolbar.addAction(self.eraserTool)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.lineTool)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.paintBucketTool)
        