from util import utility
from Solr.MIME import MIME_Core
import json

class Visulization(object):

    def __init__(self):
        self.SOLR = MIME_Core()
        self.sizes = utility.constant.FILE_SIZE
        self.size_mapping = utility.constant.SIZE_MAPPING

    def extractMIME(self):
        FileSizeList = []

        # Getting the files whose size would be computed
        response = MIME_Core().facetQuery('metadata')
        mimeTypeResponse = response.result.dict['facet_counts']['facet_fields']['metadata']

        out_file = open('mime.json',"w")

        mimeCount = {}
        for mime, count in mimeTypeResponse.iteritems():
            mimeCount[mime]= [count]
        json.dump(mimeCount,out_file, indent=4)


    def addSize(self):
        size = self.extractMIME()
        print '\n\nStarting to index the filesize of the dataset'
        self.SOLR.index(size)
        print '\nIndexed!'

if __name__ == '__main__':
    Visulization().extractMIME()