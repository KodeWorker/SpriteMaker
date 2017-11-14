from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit

class CanvasWidget(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.InitCanvas()
        
    def InitCanvas(self):    
        vbox = QVBoxLayout(self)
        vbox.setContentsMargins(0, 0, 0, 0)
        canvasLog = QTextEdit('Canvas')
        vbox.addWidget(canvasLog)
        self.setLayout(vbox)

