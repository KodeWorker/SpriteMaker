""" Sprite Sheet Control
# Description:
    This scrpit contains the classes/functions of file system of a sprite 
    sheet.
# Author: Shin-Fu (Kelvin) Wu <fxp61005@gmail.com>
# Date: 2017/11/17
# Reference: https://docs.scipy.org/doc/numpy-1.10.1/user/basics.subclassing.html
"""

from numpy import ndarray
from PyQt5.QtGui import QColor

class SpriteSheetControl(object):
    """ Sprite Sheet Control Class
        This class controls the sprite sheet.
        
        Parameters
        ----------
        width: int
            The width of each sprite in the sheet.
        height: int
            The height of each sprite in the sheet.
        fps: int
            The Frame-Per-Second of the sprite sheet.
        initSprite: Sprite, default=None
            The initial sprite in the sheet
    """
    
    def __init__(self, width, height, fps, initSprite=None):
        self.width = width
        self.height = height
        self.fps = fps
        if initSprite == None:
            self.initSprite = Sprite((self.width, self.height))
        elif initSprite.__class__ == Sprite:
            self.initSprite = initSprite
        else:
            raise TypeError('Error: %s is not a Sprite' %(initSprite.__class__))
        self.InitSpriteSheetControl()
    
    def InitSpriteSheetControl(self):
        """ Initiate Sprite Sheet Control
            This method initiates the sprite sheet.
        """
        self.sheet = []
        self.ptr = 0
        self.sheet.append(self.initSprite)
    
    def DupLastSprite(self):
        """ Duplicate the Last Sprite
            This method copy the last frame in the sheet and append at the end.
        """
        self.sheet.append(self.sheet[-1].copy())
    
class Sprite(ndarray):
    """ Sprite Class
        This class is an array of QColors.
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.InitSprite()
    
    # Numpy.ndarray is generated in __new__() method
    def __new__(cls, *args, **kwargs):
        kwargs['dtype'] = object
        return ndarray.__new__(cls, *args, **kwargs)
    
    def InitSprite(self):
        # Fill transparent pixels
        self.fill(QColor(0, 0, 0, 0))