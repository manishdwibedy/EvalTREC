import FileSizeDiversityExtraction, FileSize
from util import constant
import URL_Shortner

def getFileSizeInfo():
    """
    Would extract the document's mime type and size of the file
    :return: a list of object having the needed data
    """
    FileSizeDiversityExtractionObj = FileSizeDiversityExtraction.FileSizeDiversityExtraction(constant.DATA_DIR)
    mimeInfo = FileSizeDiversityExtractionObj.extractMIME()

    file_size_list = []

    for mime in mimeInfo:
        filename = mime.filename
        filesize = FileSizeDiversityExtractionObj.extractSize(filename)

        file_size_obj = {
            'id': URL(mime.filename),
            'filename': mime.filename,
            'mime': mime.mimeType,
            'filesize': filesize
        }
        file_size_list.append(file_size_obj)

    return file_size_list

def URL(filename):
    """
    Would return the shortened URL for the document
    :param filename: the file getting a short URL
    :return: the short URL
    """
    return URL_Shortner.hashID(filename)
