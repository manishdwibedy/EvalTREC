import FileSizeDiversityExtraction, FileSize
from util import constant

if __name__ == '__main__':

    FileSizeDiversityExtractionObj = FileSizeDiversityExtraction.FileSizeDiversityExtraction(constant.DATA_DIR)
    mimeInfo = FileSizeDiversityExtractionObj.extractMIME()

    file_size_list = []

    for mime in mimeInfo:
        filename = mime.filename

        FileSize = FileSize(mime, 2)
