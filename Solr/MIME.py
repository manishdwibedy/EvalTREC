from util import constant
from solrcloudpy import SolrConnection
from solrcloudpy.utils import SolrException

class MIME_Core(object):

    def __init__(self):
        """
        Initiating a solr connection
        :return:
        """
        SOLR_IP = constant.SOLR_HOSTNAME + ':' + str(constant.SOLR_PORT)
        self.connection = SolrConnection([SOLR_IP])

        self.collection = constant.SOLR_CORE

    def index(self, documents):
        """
        Indexing the documents in the core
        :param documents: the documents to be indexed
        :return:
        """
        try:
            self.connection[self.collection].add(documents)
            self.connection[self.collection].commit()
        except SolrException:
            print 'Error'


    def query(self,query,rows=-1):
        """
        Query the core for documents
        :param query: the query string
        :param rows:  the number of rows to return
        :return: the solr response is returned
        """
        if rows == -1:
            return self.connection[self.collection].search({'q':query})
        else:
            return self.connection[self.collection].search({'q':query,'rows': rows})

    def queryAll(self):
        num_rows_response = self.connection[self.collection].search({'q': '*:*', 'rows': 0})
        num_rows = num_rows_response.result.dict['response']['numFound']


        return self.query('*:*', num_rows)

    def delete(self, query):
        """
        Deleting the documents that match the query.
        :param query: the query string
        :return: Nothing
        """
        self.connection[self.collection].delete({'q':query})
        self.connection[self.collection].commit()