
# Directory where the data is present
DATA_DIR = '/Users/manishdwibedy/PycharmProjects/MIME/final/'

# Solr Constants
SOLR_HOSTNAME = 'localhost'
SOLR_PORT = 8983
SOLR_CORE = 'mime'

FILE_SIZE = [
    '0 TO 10000',
    '10000 TO 1000000',
    '1000000 TO 10000000',
    '10000000 TO 100000000',
    '100000000 TO *'
]

SIZE_MAPPING = {
    '0 TO 10000' : '0 - 10 KB',
    '10000 TO 1000000' : '10 KB - 1 MB',
    '1000000 TO 10000000' : '1 MB - 10 MB',
    '10000000 TO 100000000' : '10 MB - 100 MB',
    '100000000 TO *' : '100 MB+'
}