import connection
from util import constant

def delete(connection, collection, query):
    """
    Deleting the documents from the collection matching the query
    :param connection: the Solr Connection
    :param collection: the Solr Collection
    :param query: Query
    :return: Nothing
    """
    connection[collection].delete({'q':query})
    connection[collection].commit()

if __name__ == '__main__':
    conn = connection.get_connection()
    delete(conn, constant.SOLR_CORE, '*:*')

