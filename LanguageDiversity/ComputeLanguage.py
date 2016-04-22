from util import utility
from Tika.getTika import Tika
from Solr.MIME import MIME_Core

class GetLanguageInformation(object):

    def __init__(self):
        self.SOLR = MIME_Core()

    def computeLanguage(self):
        """
        Computation of the mime type of all the files in the solr core
        :return: the list of MimeTpye object
        """

        LanguageList = []
        # Getting the files whose meta data would be computed
        response = MIME_Core().queryAll()
        files = response.result.dict['response']['docs']

        print 'Adding language to the dataset'
        parsedFiles = 0
        totalFiles = len(files)
        utility.printProgress(parsedFiles, totalFiles, prefix = 'Progress:', suffix = 'Complete', barLength = 50)


        tika = Tika()
        # Looping over all the files
        for file in files:
            # Computing the language type
            filelocation = file['file'][0]

            language = str(tika.getLanguage(filelocation))

            file['language'] = language

            # Appending to the list
            LanguageList.append(file)

            parsedFiles += 1
            utility.printProgress(parsedFiles, totalFiles, prefix = 'Progress:', suffix = 'Complete', barLength = 50)

        # Returning the list
        return LanguageList

    def addLanguage(self):
        language = self.computeLanguage()
        print '\n\nStarting to index the languages of the dataset'
        self.SOLR.index(language)
        print '\nIndexed!'