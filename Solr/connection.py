from solrcloudpy import SolrConnection
from util import constant

def get_connection():
    '''
    Get the solr connection.
    :return:
    '''
    SOLR_IP = constant.SOLR_HOSTNAME + ':' + str(constant.SOLR_PORT)
    connection = SolrConnection([SOLR_IP])

    return connection


if __name__ == '__main__':
    connection = get_connection()
    print connection





