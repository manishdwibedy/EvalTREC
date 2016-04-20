from Tika import getTika
from util import utility
from Solr.MIME import MIME_Core
import sys

class Parser(object):

    def __init__(self):
        pass

    def getMetaData(self):
        # Getting the files whose meta data would be computed
        response = MIME_Core().query('*:*')
        files = response.result.dict['response']['docs']

        # Getting the tika object
        tikaObj = getTika.Tika()

        # Computing the meta data
        for file in files:
            filelocation = file['filename'][0]
            metadata = tikaObj.getMetaData(filelocation)
            print metadata
            print sys.getsizeof(metadata)
            pass