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

        mimeList = []
        for mime_type, count in mimeTypeResponse.iteritems():
            mimeList.append(mime_type)


        mime_size_diversity = {}
        for mime in mimeList:
            jsonObj = {}
            print mime[mime.index('/')+1:]
            for size in self.sizes:
                query = 'metadata:%s AND size:[%s]' % (mime, size)
                response = MIME_Core().queryAll(query=query)
                files = response.result.dict['response']['docs']
                jsonObj[self.size_mapping[size]] = [len(files)]
            mime_size_diversity[mime] = jsonObj

            out_file = open('data/'+mime[mime.index('/')+1:]+'.json',"w")

            json.dump(jsonObj,out_file, indent=4)


    def addSize(self):
        size = self.extractMIME()
        print '\n\nStarting to index the filesize of the dataset'
        self.SOLR.index(size)
        print '\nIndexed!'

if __name__ == '__main__':
    Visulization().extractMIME()