from MimeDiversity import ComputeMIME
import os

class FileSizeDiversityExtraction(object):

    def __init__(self, directory):
        self.directory = directory

    def extractMIME(self):
        mime = ComputeMIME.GetMIMEInformation(self.directory)

        mimeInfo = mime.computeMIME()
        return mimeInfo

    def extractSize(self, filename):
        try:
            return os.path.getsize(filename)
        except OSError:
            return -1