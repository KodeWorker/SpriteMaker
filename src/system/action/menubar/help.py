""" Help Actions Control
# Description:
    This script contains all the classes/functions related to help actions in 
    menu bar.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/11/15
"""
class HelpControl(object):
    """ Help Control Class
        This contains the window actions related to help options.
    """
    
    def ReportIssue(self):
        print('[Action] Help -> Report issue ...')
    
    def AboutSpriteMaker(self):
        print('[Action] Help -> About SpriteMaker')