from MimeDiversity import ComputeMIME
from util import utility

class FileSizeDiversityExtraction(object):

    def __init__(self, directory):
        self.directory = directory

    def extractMIME(self):
        mime = ComputeMIME.GetMIMEInformation(self.directory)

        mimeInfo = mime.computeMIME()
        pass

    def extractSize(self, filename):
        pass