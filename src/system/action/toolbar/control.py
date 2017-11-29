""" Tool Bar Control
# Description:
    This scrpit contains the actions of all tool bar elements.
# Author: Shin-Fu (Kelvin) Wu <fxp61005@gmail.com>
# Date: 2017/11/15
"""
from src.system.action.base import BaseController

class ToolBarControl(BaseController):
    """ Tool Bar Control Class
        This class contains all the actions of each menu bar action.
    """
    
    def CursorTool(self):
        if self.enable:
            print('[TOOL] Cursor mode')

    def PenTool(self):
        if self.enable:
            print('[TOOL] Pen mode')
    
    def EraserTool(self):
        if self.enable:
            print('[TOOL] Erasor mode')
    
    def LineTool(self):
        if self.enable:
            print('[TOOL] Line mode')
    
    def PaintBucketTool(self):
        if self.enable:
            print('[TOOL] Paint Bucket mode')