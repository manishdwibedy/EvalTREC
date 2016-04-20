from Tika import tika
from util import utility

class Parser(object):

    def __init__(self, directory):
        self.directory = directory

    def getMetaData(self):
        MIMEList = []

        # Getting all the files in the directory
        files = utility.getFilesInDirectory(self.directory)
        print 'Got', str(len(files)), 'file(s).'

