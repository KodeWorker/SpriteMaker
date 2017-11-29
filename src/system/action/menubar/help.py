""" Help Actions Control
# Description:
    This script contains all the classes/functions related to help actions in 
    menu bar.
# Author: Shin-Fu (Kelvin) Wu <fxp61005@gmail.com>
# Date: 2017/11/21
"""

from src.system.action.base import BaseController

class HelpControl(BaseController):
    """ Help Control Class
        This contains the window actions related to help options.
    """        
    def ReportIssue(self):
        if self.enable:
            print('[Action] Help -> Report issue ...')
    
    def AboutSpriteMaker(self):
        if self.enable:
            print('[Action] Help -> About SpriteMaker')