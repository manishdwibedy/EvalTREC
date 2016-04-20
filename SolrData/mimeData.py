from util import utility
import URL_Shortner
from Solr.MIME import MIME_Core

class MIME(object):

    def __init__(self, directory):
        self.directory = directory
        self.MIME = MIME_Core()

    def loadData(self):
        solr_data = []
        files = utility.getFilesInDirectory(self.directory)

        for file in files:
            fileObj = {
                'file' : file,
                'id': URL_Shortner.hashID(file)
            }
            solr_data.append(fileObj)

        self.MIME.index(solr_data)
