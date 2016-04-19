import FileSizeDiversityExtraction, FileSize
from util import constant

if __name__ == '__main__':

    FileSizeDiversityExtractionObj = FileSizeDiversityExtraction.FileSizeDiversityExtraction(constant.DATA_DIR)
    mimeInfo = FileSizeDiversityExtractionObj.extractMIME()

    file_size_list = []

    for mime in mimeInfo:
        filename = mime.filename
        filesize = FileSizeDiversityExtractionObj.extractSize(filename)
        file_size = FileSize.FileSize(mime, filesize)
        file_size_list.append(file_size)

    pass
