from MimeDiversity import MimeType

class FileSize(object):
    """
    The model class holding the filesize object
    """
    def __init__(self, mimeObj, size):
        self.mimeObj = mimeObj
        self.size = size

    def getInfo(self):
        print "Filename - " + self.mimeObj.filename
        print "MIME - " + self.mimeObj.mime
        print "size - " + self.size

    def __str__(self):
        return "File - '%s' has a mime type of %s and file size of %d bytes" % (self.mimeObj.filename, self.mimeObj.mimeType, self.size)