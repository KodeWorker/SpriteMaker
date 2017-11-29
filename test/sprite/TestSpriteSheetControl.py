""" Unittest for Sprite Sheet Control
# Description:
    Unit test for accessment and funtionality of Sprite Sheet Control.
# Author: Shin-Fu (Kelvin) Wu <fxp61005@gmail.com>
# Date: 2017/11/29
"""
import unittest

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.system.sprite.control import SpriteSheetControl, Sprite

from PyQt5.QtGui import QColor

class TestSpriteSheetControl(unittest.TestCase):
    unittest.TestLoader.testMethodPrefix = 'Test'
    
    width = 8
    height = 6
    fps = 30
    spriteSheetControl = SpriteSheetControl(width, height, fps)

    def TestParameterAccess(self):
        self.assertEqual(self.width, self.spriteSheetControl.width)
        self.assertEqual(self.height, self.spriteSheetControl.height)
        self.assertEqual(self.fps, self.spriteSheetControl.fps)
        self.assertEqual(self.spriteSheetControl.initSprite.__class__,
                         Sprite)
    
    def TestAtrributeAccess(self):
        self.assertEqual(self.spriteSheetControl.sheet.__class__, list)
        self.assertEqual(self.spriteSheetControl.ptr.__class__, int)
    
    def TestDupLastSprite(self):
        currentSheetSize = len(self.spriteSheetControl.sheet)
        self.spriteSheetControl.DupLastSprite()
        
        # Check the duplication
        self.assertEqual(len(self.spriteSheetControl.sheet),
                         currentSheetSize + 1)        
        # Check the duplicated sprite is not just a reference
        self.spriteSheetControl.sheet[0][0,0] = QColor(1,1,1,1)
        self.assertNotEqual(self.spriteSheetControl.sheet[0][0,0],
                            self.spriteSheetControl.sheet[1][0,0])
        
if __name__ == '__main__':
    unittest.main(verbosity=2)