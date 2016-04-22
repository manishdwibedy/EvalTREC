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

        tika = Tika()
        # Looping over all the files
        for file in files:
            # Computing the language type
            filelocation = file['file'][0]

            language = str(tika.getLanguage(filelocation))

            file['language'] = language

            # Appending to the list
            LanguageList.append(file)

        # Returning the list
        return LanguageList

    def addMime(self):
        language = self.computeLanguage()

        self.SOLR.index(language)