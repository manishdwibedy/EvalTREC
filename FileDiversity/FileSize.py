from MimeDiversity import MimeType

class FileSize(MimeType.MIME):
    """
    The model class holding the filesize object
    """
    def __init__(self, filename, mimeType, size):
        MimeType.__init__(self, filename, mimeType)
        self.size = size

    def getInfo(self):
        print "Filename - " + self.filename
        print "MIME - " + self.mime
        print "size - " + self.size

    def __str__(self):
        return "File - '%s' has a mime type of %s and file size of %s bytes" % (self.filename, self.mimeType, self.size)