""" Menu Bar Manager
# Description:
    This scrpit contains the higher-level control of all menu bar actions.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/11/15
"""

from src.system.action.menubar.file import FileManager
from src.system.action.menubar.help import HelpManager

class MenuBarManager(FileManager, HelpManager):
    """ Menu Bar Manager Class
        This class contains all the managers of each menu bar element.
    """
    
    pass

