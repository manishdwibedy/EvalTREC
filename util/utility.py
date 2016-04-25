import os
import sys
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

# Reference : http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
# Print iterations progress
def printProgress (iteration, total, prefix = 'Progress', suffix = 'Complete', decimals = 2, barLength = 100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
    """
    filledLength    = int(round(barLength * iteration / float(total)))
    percents        = round(100.00 * (iteration / float(total)), decimals)
    bar             = '#' * filledLength + '-' * (barLength - filledLength)
    print '%s [%s] %s%s %s\r' % (prefix, bar, percents, '%', suffix)
    if iteration == total:
        print("\n")