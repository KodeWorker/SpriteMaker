from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit

class FrameWidget(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.InitFrame()
        
    def InitFrame(self):    
        vbox = QVBoxLayout(self)
        vbox.setContentsMargins(0, 0, 0, 0)
        canvasLog = QTextEdit('Frame')
        vbox.addWidget(canvasLog)
        self.setLayout(vbox)