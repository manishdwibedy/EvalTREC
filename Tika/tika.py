from tika import detector, parser

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
        parsed = parser.from_file(filename)
        return parsed