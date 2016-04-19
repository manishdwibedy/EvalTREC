import os
from util import constant

def getFilesInDirectory(directory=constant.DATA_DIR):
    """
    A utility method to get the files in the directory
    :param directory: the directory being explored
    :return: a list of file in the directory
    """
    files = []

    for rootDirectory, directories, fileList in os.walk(directory):
        for file in fileList:
            if not file.startswith('.'):
                files.append(os.path.join(rootDirectory, file))

    return files