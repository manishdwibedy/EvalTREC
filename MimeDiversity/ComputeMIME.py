from util import utility
from tika import detector
from Solr.MIME import MIME_Core

class GetMIMEInformation(object):

    def __init__(self):
        self.SOLR = MIME_Core()

    def computeMIME(self):
        """
        Computation of the mime type of all the files in the solr core
        :return: the list of MimeTpye object
        """

        ContentTypeList = []
        # Getting the files whose meta data would be computed
        response = MIME_Core().query('*:*')
        files = response.result.dict['response']['docs']

        # Looping over all the files
        for file in files:
            # Computing the mime type
            contentType = str(detector.from_file(file['file'][0]))

            file['metadata'] = contentType

            # Appending to the list
            ContentTypeList.append(file)

        # Returning the list
        return ContentTypeList

    def addMime(self):
        mime = self.computeMIME()

        self.SOLR.index(mime)