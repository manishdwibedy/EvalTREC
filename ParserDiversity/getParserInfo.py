from Tika import getTika
from util import utility
from Solr.MIME import MIME_Core
import sys

class Parser(object):

    def __init__(self):
        self.SOLR = MIME_Core()

    def getMetaData(self):
        metadataList = []
        # Getting the files whose meta data would be computed
        response = MIME_Core().query('*:*')
        files = response.result.dict['response']['docs']

        # Getting the tika object
        tikaObj = getTika.Tika()

        # Computing the meta data
        for file in files:
            filelocation = file['file'][0]
            metadata = tikaObj.getMetaData(filelocation)
            file['metadata_size'] = sys.getsizeof(metadata)

            metadataList.append(file)

        return metadataList

    def addMetaDataSize(self):
        metadatasize = self.getMetaData()

        self.SOLR.index(metadatasize)