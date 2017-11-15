from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit

class ColorWheelWidget(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.InitColorWheel()
        
    def InitColorWheel(self):    
        vbox = QVBoxLayout(self)
        vbox.setContentsMargins(0, 0, 0, 0)
        canvasLog = QTextEdit('ColorWheel')
        vbox.addWidget(canvasLog)
        self.setLayout(vbox)
