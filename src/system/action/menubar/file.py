""" File Action Control
# Description:
    This script contains all the classes/functions related to file system 
    actions in menu bar.
# Author: Shin-Fu (Kelvin) Wu <fxp61005@gmail.com>
# Date: 2017/11/21
"""

from src.system.action.base import BaseController

class FileControl(BaseController):
    """ File Control Class
        This contains the window actions related to file system.
        
    """
        
    def NewAct(self):
        if self.enable:
            print('[Action] File -> New')

    def OpenAct(self):
        if self.enable:
            print('[Action] File -> Open ...')
    
    def SaveAct(self):
        if self.enable:
            print('[Action] File -> Save')
        
    def SaveAllAct(self):
        if self.enable:
            print('[Action] File -> Save all')
        
    def SaveAsAct(self):
        if self.enable:
            print('[Action] File -> Save as ...')
    
    def CloseAct(self):
        if self.enable:
            print('[Action] File -> Close')
    
    def CloseAllAct(self):
        if self.enable:
            print('[Action] File -> Close all')
    
    def QuitAct(self):
        if self.enable:
            print('[Action] File -> Quit')
