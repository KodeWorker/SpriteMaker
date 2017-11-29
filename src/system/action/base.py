""" Base Controller
# Description:
    This script is a basic controller class.
# Author: Shin-Fu (Kelvin) Wu <fxp61005@gmail.com>
# Date: 2017/11/21
"""

class BaseController(object):
    """ Base Controller Class
        This is a interface for basic controllers.
    
        Parameters
        ----------
        enable: bool
            This is a flag to enable the action controller.
    """
    def __init__(self, enable=True):
        self.enable = enable