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

        readFiles = 0
        totalFiles = len(files)

        print 'Adding files to SOLR'
        utility.printProgress(readFiles, totalFiles, prefix = 'Progress:', suffix = 'Complete', barLength = 50)

        for file in files:
            fileObj = {
                'file' : file,
                'shortURL': URL_Shortner.hashID(file)
            }
            solr_data.append(fileObj)
            readFiles += 1
            utility.printProgress(readFiles, totalFiles, prefix = 'Progress:', suffix = 'Complete', barLength = 50)

        print '\n\nStarting to index..'
        self.MIME.index(solr_data)
        print '\nIndexed!'
