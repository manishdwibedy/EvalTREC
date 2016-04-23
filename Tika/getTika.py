from tika import detector, parser
import tika

import sys
import os
from tika import language

class Tika(object):

    def __init__(self):
        pass

    def getMimeType(self, filename):
        """
        Get the MIME type of the file.
        :param filename:
        :return:
        """
        mime_type = detector.from_file(filename)

        return str(mime_type)

    def getMetaData(self, filename):
        parsed = parser.from_file(filename)
        return parsed["metadata"]

    def getContent(self, filename):
        parsed = parser.from_file(filename)
        return parsed["content"]

    def getParse(self, filename):
        # Getting the parsed content
        parsed = parser.from_file(filename)

        return parsed

    def getLanguage(self, filename):
        # To avoid printing to the console
        sys.stdout = open(os.devnull, "w")

        # Getting the language for the document
        language = tika.language.from_file(filename)

        # To avoid printing to the console
        sys.stdout = sys.__stdout__

        return language