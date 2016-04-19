from util import utility
from tika import detector
from MimeDiversity import MimeType

class GetMIMEInformation(object):

    def __init__(self, directory):
        self.directory = directory

    def computeMIME(self):
        """
        Computation of the mime type of all the files
        :return: the list of MimeTpye object
        """
        MIMEList = []

        # Getting all the files in the directory
        files = utility.getFilesInDirectory(self.directory)
        print 'Got', str(len(files)), 'file(s).'

        # Looping over all the files
        for file in files:
            # Computing the mime type
            mimeTpye = str(detector.from_file(file))

            # Creating the MIME dataobject
            mimeObj = MimeType.MIME(file, mimeTpye)

            # Appending to the list
            MIMEList.append(mimeObj)

        # Returning the list
        return MIMEList