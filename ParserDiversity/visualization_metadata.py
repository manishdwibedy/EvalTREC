from util import utility
from Solr.MIME import MIME_Core
import json
from tika import parser
import operator

class Visulization(object):

    def __init__(self):
        self.SOLR = MIME_Core()
        self.sizes = utility.constant.FILE_SIZE
        self.size_mapping = utility.constant.SIZE_MAPPING

    def extractParsingInfo(self):
        FileSizeList = []

        # Getting the files whose size would be computed
        response = MIME_Core().facetQuery('metadata')
        mimeTypeResponse = response.result.dict['facet_counts']['facet_fields']['metadata']


        mimeList = []
        for mime_type, count in mimeTypeResponse.iteritems():
            if mime_type == 'application/java-archive':
                continue
            mimeList.append(mime_type)


        mime_size_diversity = {}
        for mime in mimeList:
            metadata_list = {}
            print mime[mime.index('/')+1:]

            query = 'metadata:%s' % (mime)
            response = MIME_Core().queryAll(query=query, rows = 100)
            files = response.result.dict['response']['docs']

            for file in files:
                parsed = parser.from_file(file['file'][0])
                if 'metadata' in parsed:
                    metadata = parsed['metadata']

                    for key,value in metadata.iteritems():
                        if key in mime_size_diversity:
                            mime_size_diversity[key] += 1
                        else:
                            mime_size_diversity[key] = 1
                    pass
            print 'done with ' + mime

        top_metadata = sorted(mime_size_diversity.items(), key=operator.itemgetter(1), reverse=True)

        metadata = []
        for item in top_metadata[:20]:
            metadata.append(item[0])
            metadata.append(item[1])
            pass

        out_file = open('data/word_cloud/word_cloud.json',"w")
        json.dump(metadata,out_file, indent=4)


        pass


if __name__ == '__main__':
    Visulization().extractParsingInfo()