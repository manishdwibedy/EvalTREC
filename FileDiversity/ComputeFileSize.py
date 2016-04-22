from util import utility
from tika import detector
from Solr.MIME import MIME_Core
import os

class FileSize(object):

    def __init__(self):
        self.SOLR = MIME_Core()

    def extractSize(self):
        FileSizeList = []

        # Getting the files whose size would be computed
        response = MIME_Core().queryAll()
        files = response.result.dict['response']['docs']

        fileIndex = 0
        totalFiles = len(files)

        print 'Adding filesize to the dataset'
        utility.printProgress(fileIndex, totalFiles, prefix = 'Progress:', suffix = 'Complete', barLength = 50)


        # Looping over all the files
        for file in files:
            # Computing the file size
            try:
                file['size'] = os.path.getsize(file['file'][0])
            except OSError:
                return -1

            FileSizeList.append(file)

            fileIndex += 1
            utility.printProgress(fileIndex, totalFiles, prefix = 'Progress:', suffix = 'Complete', barLength = 50)

        return FileSizeList

    def addSize(self):
        size = self.extractSize()
        print '\n\nStarting to index the filesize of the dataset'
        self.SOLR.index(size)
        print '\nIndexed!'