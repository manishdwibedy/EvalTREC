from util import utility
from Solr.MIME import MIME_Core
import json

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
            metadata_size = {}
            content_size = {}
            parser_count = {}
            print mime[mime.index('/')+1:]

            for size in self.sizes:
                query = 'metadata:%s AND size:[%s]' % (mime, size)
                response = MIME_Core().queryAll(query=query)
                files = response.result.dict['response']['docs']

                avg_content_size = 0
                avg_metadata_size = 0

                for file in files:
                    avg_metadata_size += file['metadata_size'][0]
                    avg_content_size += file['content_size'][0]

                    if 'parsers' in file:
                        for parser in file['parsers']:
                            if parser in parser_count:
                                parser_count[parser] += 1
                            else:
                                parser_count[parser] = 1
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