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
        response = MIME_Core().queryAll()
        files = response.result.dict['response']['docs']

        # Getting the tika object
        tikaObj = getTika.Tika()

        print 'Adding metadata_size, content_size and parsers to the dataset'

        parsedFiles = 0
        totalFiles = len(files)
        utility.printProgress(parsedFiles, totalFiles, prefix = 'Progress:', suffix = 'Complete', barLength = 50)

        # Computing the meta data
        for file in files:
            filelocation = file['file'][0]
            parsed = tikaObj.getParse(filelocation)

            if 'metadata' in parsed:
                metadata = parsed['metadata']
                file['metadata_size'] = sys.getsizeof(metadata)
                parsers = metadata['X-Parsed-By']
                file['parsers'] = parsers
            else:
                file['metadata_size'] = -1

            if 'content' in parsed:
                content = parsed['content']
                file['content_size'] = sys.getsizeof(content)
            else:
                file['content_size'] = -1

            metadataList.append(file)
            parsedFiles += 1
            utility.printProgress(parsedFiles, totalFiles, prefix = 'Progress:', suffix = 'Complete', barLength = 50)


        return metadataList

    def addMetaDataSize(self):
        metadatasize = self.getMetaData()
        print '\n\nStarting to index the sizes of the dataset'
        self.SOLR.index(metadatasize)
        print '\nIndexed!'
