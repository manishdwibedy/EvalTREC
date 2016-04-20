from tika import detector

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
