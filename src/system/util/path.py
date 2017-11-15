""" Path Utilities
# Description:
    This script contains all the classes/functions related to file path.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/11/15
"""
import os

def RelativePath(relativePath, *args):
    """ Relative Path
        This function returns the relative path from current working path.
        
        Parameters
        ----------
        relativePath: str
            This is the relative path to access.
        *args: str
            Sub-folder from previous argument.
        
        Returns
        -------
        dirPath: str
            The joined path of all arguments.
    """
    # Get current absolute path
    basePath = os.path.abspath('.')
    dirPath = os.path.join(basePath, relativePath)
    # Append all arguments
    for arg in args:
        dirPath = os.path.join(dirPath, arg)

    return dirPath