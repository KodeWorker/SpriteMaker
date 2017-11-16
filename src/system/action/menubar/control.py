""" Menu Bar Control
# Description:
    This scrpit contains the higher-level control of all menu bar actions.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/11/15
"""

from src.system.action.menubar.file import FileControl
from src.system.action.menubar.help import HelpControl

class MenuBarControl(FileControl, HelpControl):
    """ Menu Bar Control Class
        This class contains all the controls of each menu bar action.
    """