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
        response = MIME_Core().query('*:*')
        files = response.result.dict['response']['docs']


        # Looping over all the files
        for file in files:
            # Computing the file size
            try:
                file['size'] = os.path.getsize(file['file'][0])
            except OSError:
                return -1

            FileSizeList.append(file)

        return FileSizeList

    def addSize(self):
        size = self.extractSize()

        self.SOLR.index(size)