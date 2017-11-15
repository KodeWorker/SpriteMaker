""" BATCH TEST ON ALL UNIT TESTS
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

def Main():
    # Argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', 
                        help='This folder contains all the unittest files',
                        type=str)
    args = parser.parse_args()
    
    # Files in the Directory
    current_script = os.path.basename(__file__)    
    test_files = [x[2] for x in os.walk(args.dir)][0]
    testmodules = [x[:-3] for x in test_files if x != current_script and
                   not x.endswith('.sh') and not x.endswith('.bat')]
    suite = unittest.TestSuite()
    
    # Run unit tests
    for t in testmodules:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(t, globals(), locals(), ['suite'])
            suitefn = getattr(mod, 'suite')
            suite.addTest(suitefn())
        except (ImportError, AttributeError):
            # else, just load all the test cases from the module.
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

    unittest.TextTestRunner().run(suite)
    
if __name__ == '__main__':
    Main()



