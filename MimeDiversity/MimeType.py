
class MIME(object):
    """
    The model class for holding the MIME information
    """
    def __init__(self, filename, mimeTpye):
        self.filename = filename
        self.mimeType = mimeTpye

    def __str__(self):
        return "File -'%s' has the mime type of %s" % (self.filename, self.mimeType)
