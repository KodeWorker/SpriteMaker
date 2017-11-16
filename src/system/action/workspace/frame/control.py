""" Frame Control
# Description:
    This scrpit contains the actions of all elements in frame workspace.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/11/15
"""

class FrameControl(object):
    """ Frame Manager Class
        This class contains all the actions of in frame workspace.
    """
    
    def PlayAct(self):
        print('[Action] Frame -> Play')
        
    def StopAct(self):
        print('[Action] Frame -> Stop')
    
    def LoopAct(self):
        if self.loopBtn.isChecked():
            print('[Action] Frame -> Loop On')
        else:
            print('[Action] Frame -> Loop Off')
