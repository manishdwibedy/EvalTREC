import os
from util import constant

def getFilesInDirectory(directory=constant.DATA_DIR):
    """
    A utility method to get the files in the directory
    :param directory: the directory being explored
    :return: a list of file in the directory
    """
    files = []

    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            files.append(os.path.join(root, name))

    return files