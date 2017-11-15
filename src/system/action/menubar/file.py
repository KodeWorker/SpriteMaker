""" File Action Manager
# Description:
    This script contains all the classes/functions related to file system in 
    menu bar.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/11/15
"""

class FileManager(object):
    """ File Manager Class
        This contains the window actions related to file system.
    """
    
    def NewAct(self):
        print('[Action] File -> New')

    def OpenAct(self):
        print('[Action] File -> Open ...')
    
    def SaveAct(self):
        print('[Action] File -> Save')
        
    def SaveAllAct(self):
        print('[Action] File -> Save all')
        
    def SaveAsAct(self):
        print('[Action] File -> Save as ...')
    
    def CloseAct(self):
        print('[Action] File -> Close')
    
    def CloseAllAct(self):
        print('[Action] File -> Close all')
    
    def QuitAct(self):
        print('[Action] File -> Quit')
