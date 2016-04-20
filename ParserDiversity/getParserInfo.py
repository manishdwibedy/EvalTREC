from Tika import getTika
from util import utility
from Solr.MIME import MIME_Core
import sys

class Parser(object):

    def __init__(self, directory, readFromSolr):
        self.directory = directory
        self.readFromSolr = readFromSolr

    def getMetaData(self):
        MIMEList = []

        if not self.readFromSolr:
            # Reading all the files in the directory
            files = utility.getFilesInDirectory(self.directory)
            print 'Got', str(len(files)), 'file(s).'

        tikaObj = getTika.Tika()
        response = MIME_Core().query('*:*')
        files = response.result.dict['response']['docs']
        for file in files:
            filelocation = file['filename'][0]
            metadata = tikaObj.getMetaData(filelocation)
            print metadata
            print sys.getsizeof(metadata)
            pass