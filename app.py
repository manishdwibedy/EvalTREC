# SOLR Mime Core
from Solr.MIME import MIME_Core

# Importing the data directory
from util.constant import DATA_DIR

# MIME Modue
from MimeDiversity import ComputeMIME

# Parser Module
from ParserDiversity.getParserInfo import Parser

# The files to be loaded into solr
from SolrData import mimeData

from FileDiversity import ComputeFileSize

# Flag to control clearing the solr index
resetSolrData = False

# Various Flags to control which module would run
computeFileSize = True
commuteMIME = True
commuteParser = True

if __name__ == '__main__':
    mime = MIME_Core()

    if resetSolrData:
        mime.delete('*:*')

    if resetSolrData:
        # Loading the files into solr
        mimeData.MIME(DATA_DIR).loadData()

    if commuteMIME:
        ComputeMIME.GetMIMEInformation().addMime()

    if computeFileSize:
        size = ComputeFileSize.FileSize().addSize()

    if commuteParser:
        parser = Parser().addMetaDataSize()
