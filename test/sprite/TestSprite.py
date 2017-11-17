import unittest

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.system.sprite.control import Sprite

from PyQt5.QtGui import QColor

class TestSprite(unittest.TestCase):
    unittest.TestLoader.testMethodPrefix = 'Test'
    
    width = 8
    height = 6
    sprite = Sprite((width, height))

    def TestParameterAccess(self):
        self.assertEqual(self.sprite.shape, (self.width, self.height))        
        
    def TestAtrributeAccess(self):
        self.assertEqual(self.sprite[0, 0].__class__, QColor)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)