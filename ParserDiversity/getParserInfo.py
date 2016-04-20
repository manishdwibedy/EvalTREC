from Tika import getTika
from util import utility
from Solr.MIME import MIME_Core
import sys

class Parser(object):

    def __init__(self, directory):
        self.directory = directory

    def getMetaData(self):
        MIMEList = []

        tikaObj = getTika.Tika()
        response = MIME_Core().query('*:*')
        files = response.result.dict['response']['docs']
        for file in files:
            filelocation = file['filename'][0]
            metadata = tikaObj.getMetaData(filelocation)
            print metadata
            print sys.getsizeof(metadata)
            pass