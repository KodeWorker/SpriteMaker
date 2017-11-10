import os

def RelativePath(relativePath, *args):
    basePath = os.path.abspath('.')

    dirPath = os.path.join(basePath, relativePath)
    for arg in args:
        dirPath = os.path.join(dirPath, arg)

    return dirPath