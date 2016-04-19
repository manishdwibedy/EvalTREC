from util import utility

class ComputeMIME(object):

    def __init__(self, directory):
        self.directory = directory

    def computeMIME(self):
        MIMEList = []

        files = utility.getFilesInDirectory(self.directory)
