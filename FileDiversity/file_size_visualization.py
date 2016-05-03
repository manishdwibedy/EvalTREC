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
        jsonObj = {}
        mimeCount = {}
        for mime in mimeList:

            print mime[mime.index('/')+1:]

            file_size = 0
            query = 'metadata:%s' % (mime)
            if 'html' in mime:
                response = MIME_Core().queryAll(query=query, rows=13000)
            else:
                response = MIME_Core().queryAll(query=query)
            files = response.result.dict['response']['docs']

            mimeCount[mime] = len(files)
            for file in files:
                file_size += file['size'][0] / float(200000000)

            if mimeCount[mime] != 0:
                jsonObj[mime] = [float(file_size)/mimeCount[mime]]
            else:
                jsonObj[mime] = [0]
        mime_size_diversity[mime] = jsonObj

        output = []
        for mime, count in jsonObj.iteritems():
            output.append(count[0])

        out_file = open('data/ratio/ratio.json',"w")

        json.dump({
            'ratio': output
        },out_file, indent=4)

        mimeList = []
        out_file = open('data/ratio/ratio_units.json',"w")
        for mime, count in mimeCount.iteritems():
            mimeList.append(mime)
        json.dump(mimeList,out_file, indent=4)

    def addSize(self):
        size = self.extractMIME()
        print '\n\nStarting to index the filesize of the dataset'
        self.SOLR.index(size)
        print '\nIndexed!'

if __name__ == '__main__':
    Visulization().extractMIME()