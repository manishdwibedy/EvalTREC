from FileDiversity import extractFileSizeDiversity
from Solr.MIME import MIME_Core


if __name__ == '__main__':
    mime = MIME_Core()

    file_size = extractFileSizeDiversity.getFileSizeInfo()
    mime.index(file_size)
