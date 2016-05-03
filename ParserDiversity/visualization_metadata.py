from util import utility
from Solr.MIME import MIME_Core
import json
from tika import parser

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
            mimeList.append(mime_type)


        mime_size_diversity = {}
        for mime in mimeList:
            metadata_list = {}
            print mime[mime.index('/')+1:]

            query = 'metadata:%s' % (mime)
            response = MIME_Core().queryAll(query=query, rows = 10)
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

        if len(files) != 0:
            metadata_size[self.size_mapping[size]] = [avg_metadata_size / len(files)]
            content_size[self.size_mapping[size]] = [avg_content_size / len(files)]

        else:
            metadata_size[self.size_mapping[size]] = 0
            content_size[self.size_mapping[size]] = 0


            out_file = open('data/metadata/'+mime[mime.index('/')+1:]+'.json',"w")
            json.dump(metadata_size,out_file, indent=4)

            out_file = open('data/content/'+mime[mime.index('/')+1:]+'.json',"w")
            json.dump(content_size,out_file, indent=4)

            out_file = open('data/parsers/'+mime[mime.index('/')+1:]+'.json',"w")
            json.dump(parser_count,out_file, indent=4)

            pass


if __name__ == '__main__':
    Visulization().extractParsingInfo()