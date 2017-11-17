import unittest

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.system.sprite.control import SpriteSheetControl, Sprite

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

if __name__ == '__main__':
    unittest.main(verbosity=2)