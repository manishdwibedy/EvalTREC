
class MIME(object):
    """
    The model class for holding the MIME information
    """
    def __init__(self, filename, mimeTpye):
        self.filename = filename
        self.mimeType = mimeTpye
