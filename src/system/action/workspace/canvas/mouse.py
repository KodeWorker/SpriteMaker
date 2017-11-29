""" Canvas Mouse Control
# Description:
    This scrpit contains the mouse controls of all actions in canvas workspace.
# Author: Shin-Fu (Kelvin) Wu <fxp61005@gmail.com>
# Date: 2017/11/21
"""

from PyQt5.QtCore import Qt

from src.system.action.base import BaseController

class MouseControl(BaseController):
    """ Mouse Control Class
        This class contains all the actions of in canvas workspace.
    """
    
    def mousePressEvent(self, event):
        if self.enable:
            if(event.button() == Qt.LeftButton):
                print('[Action] Canvas -> mouse left pressed @(%d,%d)' 
                      %(event.pos().x(), event.pos().y()))
            elif(event.button() == Qt.RightButton):
                print('[Action] Canvas -> mouse right pressed @(%d,%d)' 
                      %(event.pos().x(), event.pos().y()))
            elif(event.button() == Qt.MiddleButton):
                print('[Action] Canvas -> mouse middle pressed @(%d,%d)' 
                      %(event.pos().x(), event.pos().y()))
    
    def mouseMoveEvent(self, event):
        if self.enable:
            if(event.buttons() == Qt.LeftButton):
                print('[Action] Canvas -> mouse left moved @(%d,%d)' 
                      %(event.pos().x(), event.pos().y()))
            elif(event.buttons() == Qt.RightButton):
                print('[Action] Canvas -> mouse right moved @(%d,%d)' 
                      %(event.pos().x(), event.pos().y()))
            elif(event.buttons() == Qt.MiddleButton):
                print('[Action] Canvas -> mouse middle moved @(%d,%d)' 
                      %(event.pos().x(), event.pos().y()))
    
    def mouseReleaseEvent(self, event):
        if self.enable:
            if(event.button() == Qt.LeftButton):
                print('[Action] Canvas -> mouse left released @(%d,%d)' 
                      %(event.pos().x(), event.pos().y()))
            elif(event.button() == Qt.RightButton):
                print('[Action] Canvas -> mouse right released @(%d,%d)' 
                      %(event.pos().x(), event.pos().y()))
            elif(event.button() == Qt.MiddleButton):
                print('[Action] Canvas -> mouse middle released @(%d,%d)' 
                      %(event.pos().x(), event.pos().y()))
    
    def wheelEvent(self, event):
        if self.enable:
            if event.angleDelta().y() > 0:
                print('[Action] Canvas -> mouse scroll up (%d)' 
                      %(event.angleDelta().y())) 
            else:
                print('[Action] Canvas -> mouse scroll down (%d)' 
                      %(event.angleDelta().y()))