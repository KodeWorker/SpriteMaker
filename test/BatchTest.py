""" Batch Test on All Unit Tests
# Description:
    This is the batch test for all the unit test in the directory.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/11/15
# Reference: https://stackoverflow.com/questions/1732438/
             how-do-i-run-all-python-unit-tests-in-a-directory
"""

import os
import argparse
import unittest

def Test():
    # Argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', 
                        help='This folder contains all the unit test files',
                        type=str)
    args = parser.parse_args()
    
    # Files in the Directory
    currentScript = os.path.basename(os.path.abspath(__file__))
    currentScriptDir = os.path.dirname(os.path.abspath(__file__))
    
    testPath = []
    for dirPath, dirNames, fileNames in os.walk(args.dir):
        for fileName in fileNames:
            relativeDir = os.path.relpath(dirPath, currentScriptDir)
            relativeFile = os.path.join(relativeDir, fileName)
            testPath.append(relativeFile.replace('\\', '.'))
    
    testModules = [x for x in testPath if 
                   not x.endswith(currentScript) and x.endswith('.py')]
    testModules = [x.replace('.py', '') for x in testModules]
    
    suite = unittest.TestSuite()
    
    
    # Run unit tests
    for t in testModules:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(t, globals(), locals(), ['suite'])
            suitefn = getattr(mod, 'suite')
            suite.addTest(suitefn())
        except (ImportError, AttributeError):
            # else, just load all the test cases from the module.
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))
    
    unittest.TextTestRunner(verbosity=2).run(suite)
    
if __name__ == '__main__':
    Test()



