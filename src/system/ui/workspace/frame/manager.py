from configparser import ConfigParser

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon

from src.system.util.path import RelativePath
from src.system.ui.workspace.frame.base import TimeLine
from src.system.action.workspace.frame.control import FrameControl


class FrameManager(QWidget, FrameControl):
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.InitConfig()
        self.InitFrameManager()
        
    def InitConfig(self):
        config = ConfigParser()
        config.read(RelativePath('config', 'default.conf'))
        self.ratio = float(config['FRAME']['ratio'])
        self.margin = int(config['FRAME']['margin'])
        self.spacing = int(config['FRAME']['spacing'])
    
    def InitFrameManager(self):
        self.InitFrameElements()
        self.InitFrameLayout()
    
    def InitFrameElements(self):
        self.parent.frameWidget = self
        
        # Time frame view
        self.timeLine = TimeLine(self.parent)
        # Play button
        self.playBtn = QPushButton(QIcon(RelativePath('asset',
                                                      'image',
                                                      'workspace',
                                                      'frame',
                                                      'play.png')),
                                   '')
        self.playBtn.clicked[bool].connect(self.PlayAct)
        
        # Stop button
        self.stopBtn = QPushButton(QIcon(RelativePath('asset',
                                                      'image',
                                                      'workspace',
                                                      'frame',
                                                      'stop.png')),
                                   '')
        self.stopBtn.clicked[bool].connect(self.StopAct)
    
        # Loop button
        self.loopBtn = QPushButton(QIcon(RelativePath('asset',
                                                      'image',
                                                      'workspace',
                                                      'frame',
                                                      'loop.png')),
                                   '')
        self.loopBtn.clicked[bool].connect(self.LoopAct)
        self.loopBtn.setCheckable(True)
        
    def InitFrameLayout(self):
        
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.setSpacing(self.spacing)
        vbox.setSpacing(self.spacing)
        hbox.setContentsMargins(self.margin, self.margin,
                                self.margin, self.margin)
        vbox.setContentsMargins(self.margin, self.margin,
                                self.margin, self.margin)
        
        vbox.addWidget(self.playBtn)
        vbox.addWidget(self.stopBtn)
        vbox.addStretch()
        vbox.addWidget(self.loopBtn)
        hbox.addWidget(self.timeLine, self.ratio)
        hbox.addLayout(vbox, 1-self.ratio)
        
        self.setLayout(hbox)