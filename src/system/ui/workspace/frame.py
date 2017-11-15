from configparser import ConfigParser

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt

from src.system.util.path import RelativePath
from src.system.action.workspace.frame.manager import FrameManager

class FrameWidget(QWidget, FrameManager):
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.InitConfig()
        self.InitFrameElements()
        self.InitFrameLayout()
        
    def InitConfig(self):
        config = ConfigParser()
        config.read(RelativePath('config', 'default.conf'))
        self.ratio = float(config['FRAME']['ratio'])
        self.margin =int(config['FRAME']['margin'])
        
    def InitFrameElements(self):
        # Time frame view
        self.parent.timeFrame = TimeFrame(self.parent)
        # Play button
        self.parent.playBtn = QPushButton(QIcon(RelativePath('asset',
                                                      'image',
                                                      'workspace',
                                                      'frame',
                                                      'play.png')),
                                   '')
        self.parent.playBtn.clicked[bool].connect(self.PlayAct)
        
        # Stop button
        self.parent.stopBtn = QPushButton(QIcon(RelativePath('asset',
                                                      'image',
                                                      'workspace',
                                                      'frame',
                                                      'stop.png')),
                                   '')
        self.parent.stopBtn.clicked[bool].connect(self.StopAct)
    
    def InitFrameLayout(self):
        
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()        
        hbox.setContentsMargins(self.margin, self.margin,
                                self.margin, self.margin)
        vbox.setContentsMargins(self.margin, self.margin,
                                self.margin, self.margin)
        
        vbox.addWidget(self.parent.playBtn)
        vbox.addWidget(self.parent.stopBtn)
        vbox.addStretch()
        hbox.addWidget(self.parent.timeFrame, self.ratio)
        hbox.addLayout(vbox, 1-self.ratio)
        
        self.setLayout(hbox)

class TimeFrame(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.InitTimeFrame()
    
    def InitTimeFrame(self):
        qPalette = QPalette()
        qPalette.setColor(QPalette.Background, Qt.lightGray)
        self.setAutoFillBackground(True)
        self.setPalette(qPalette)