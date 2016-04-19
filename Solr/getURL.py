import connection, query
from util import constant

def getURL(filename):
    solr = connection.get_connection()
    queryURL = r'filename:(.)*' + filename

    output =  query.get(solr, constant.SOLR_CORE,  queryURL,1 )
    return output.result.dict['response']['docs'][0]['id']

if __name__ == '__main__':
    conn = connection.get_connection()
    print getURL('F81C2439341F922C5221990A7C941A251785F5F07B5BFD9E7E255C7C8A39C355')