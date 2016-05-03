from util import utility
from Solr.MIME import MIME_Core
import json

class Visulization(object):

    def __init__(self):
        self.SOLR = MIME_Core()
        self.size_mapping = utility.constant.SIZE_MAPPING

    def extractLanguage(self):
        FileSizeList = []

        # Getting the files whose size would be computed
        response = MIME_Core().facetQuery('metadata')
        mimeTypeResponse = response.result.dict['facet_counts']['facet_fields']['metadata']

        response = MIME_Core().facetQuery('language')
        LanguageResponse = response.result.dict['facet_counts']['facet_fields']['language']

        mimeList = []
        for mime_type, count in mimeTypeResponse.iteritems():
            mimeList.append(mime_type)

        languageList = []
        for language, count in LanguageResponse.iteritems():
            languageList.append(language)


        print 'id,value'
        print 'languages'
        mime_size_diversity = {}
        for mime in mimeList:
            mime_type = mime[:mime.index('/')]
            print 'languages.' + mime_type + ','
            mime_sub_type = mime[mime.index('/')+1:]
            print 'languages.'+mime_type + '.' + mime_sub_type + ','
            # print mime[mime.index('/')+1:]
            for language in languageList:
                query = 'metadata:%s AND language:%s' % (mime, language)

                if mime_sub_type =='html':
                    continue
                else:
                    response = MIME_Core().queryAll(query=query)
                files = response.result.dict['response']['docs']

                if len(files) > 0:
                    print 'languages.'+mime_type + '.' + mime_sub_type + '.'+ language + ',' + str(len(files))
            pass
        pass
        # print output
            # out_file = open('data/'+mime[mime.index('/')+1:]+'.json',"w")
            #
            # json.dump(jsonObj,out_file, indent=4)


if __name__ == '__main__':
    Visulization().extractLanguage()