""" Frame Control
# Description:
    This scrpit contains the actions of all elements in frame workspace.
# Author: Shin-Fu (Kelvin) Wu <fxp61005@gmail.com>
# Date: 2017/11/21
"""

from src.system.action.base import BaseController

class FrameControl(BaseController):
    """ Frame Control Class
        This class contains all the actions of in frame workspace.
    """
    
    def PlayAct(self):
        if self.enable:
            print('[Action] Frame -> Play')
        
    def StopAct(self):
        if self.enable:
            print('[Action] Frame -> Stop')
    
    def LoopAct(self):
        if self.enable:
            if self.loopBtn.isChecked():
                print('[Action] Frame -> Loop On')
            else:
                print('[Action] Frame -> Loop Off')
