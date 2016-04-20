from FileDiversity import extractFileSizeDiversity
from Solr.MIME import MIME_Core
from ParserDiversity.getParserInfo import Parser
from util.constant import DATA_DIR
from SolrData import mimeData

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