from FileDiversity import extractFileSizeDiversity

# SOLR Mime Core
from Solr.MIME import MIME_Core

# Importing the data directory
from util.constant import DATA_DIR

# Parser Module
from ParserDiversity.getParserInfo import Parser

# The files to be loaded into solr
from SolrData import mimeData

# Various Flags to control which module would run
computeFileSize = False
getDataFromSolr = True
resetSolrData = True

if __name__ == '__main__':
    mime = MIME_Core()

    if resetSolrData:
        mime.delete('*:*')

    # Loading the files into solr
    mimeData.MIME(DATA_DIR).loadData()

    if computeFileSize:
        file_size = extractFileSizeDiversity.getFileSizeInfo()
        mime.index(file_size)

    parser = Parser(DATA_DIR, getDataFromSolr)
    parser.getMetaData()