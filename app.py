import sys


# SOLR Mime Core
from Solr.MIME import MIME_Core

# Importing the data directory
from util.constant import DATA_DIR

# MIME Modue
from MimeDiversity import ComputeMIME

# Parser Module
from ParserDiversity.getParserInfo import Parser

# Language Module
from LanguageDiversity.ComputeLanguage import GetLanguageInformation

# Measurement Module
from MeasurementDiversity.ComputeMeasurement import GetMeasurementInformation

# The files to be loaded into solr
from SolrData import mimeData

from FileDiversity import ComputeFileSize

# override flag to override any flag set below
overrideFlag = False

# Flag to control clearing the solr index
resetSolrData = False

# Various Flags to control which module would run
computeFileSize = False
commuteMIME = False
commuteParser = False
commuteLanguage = False
commuteMeasurement = True

if __name__ == '__main__':
    mime = MIME_Core()

    orig_stdout = sys.stdout
    f = file('app.log', 'w')
    sys.stdout = f

    if overrideFlag or resetSolrData:
        mime.delete('*:*')

    if overrideFlag or resetSolrData:
        # Loading the files into solr
        mimeData.MIME(DATA_DIR).loadData()

    if overrideFlag or commuteMIME:
        ComputeMIME.GetMIMEInformation().addMime()

    if overrideFlag or computeFileSize:
        size = ComputeFileSize.FileSize().addSize()

    if overrideFlag or commuteParser:
        parser = Parser().addMetaDataSize()

    if overrideFlag or commuteLanguage:
        GetLanguageInformation().addLanguage()

    if overrideFlag or commuteMeasurement:
        GetMeasurementInformation().addMeasurement()

    sys.stdout = orig_stdout
    f.close()
