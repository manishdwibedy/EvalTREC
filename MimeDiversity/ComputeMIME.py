from util import utility

class GetMIMEInformation(object):

    def __init__(self, directory):
        self.directory = directory

    def computeMIME(self):
        MIMEList = []

        files = utility.getFilesInDirectory(self.directory)
        print 'Got', str(len(files)), 'file(s).'