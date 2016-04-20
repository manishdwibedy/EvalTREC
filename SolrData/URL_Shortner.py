import uuid
import os
from hashids import Hashids
from time import sleep
from tika import detector

bits = 8
hashids = Hashids(salt='some_complex_salt',min_length=8)

def urlShortnerUUID1():
    # print uuid.uuid3(uuid.NAMESPACE_DNS, url)
    shortURL = str(uuid.uuid1())[:bits]
    return 'http://polar.usc.edu/'+shortURL

def urlShortnerUUID4():
    # print uuid.uuid3(uuid.NAMESPACE_DNS, url)
    shortURL = str(uuid.uuid4())[:bits]
    return 'http://polar.usc.edu/'+shortURL


def hashID(url):
    intVal = 0
    for char in url:
        intVal += ord(char)
    hashid = hashids.encode(intVal)
    return hashid

def generateShortDirectory(directory_path, type):

    urlMapping = {}
    URL_Mapping = {}
    count = 0
    for subdir, dirs, files in os.walk(directory_path):
        for file in files:
            if type == 'UUID1':
                shortURL = urlShortnerUUID1()
            elif type == 'UUID4':
                shortURL = urlShortnerUUID4()
            elif type == 'HASH':
                shortURL = hashID(file)
            count += 1

            if count % 100 == 0:
                print count
            # if shortURL in urlMapping:
            #     sleep(0.1)
            #     # Again attempting to get another URL
            #     shortURL = urlShortner()
            #     if shortURL in urlMapping:
            #         print 'Again colliding'

            urlMapping[shortURL] = file
            obj = {
                'content-type': detector.from_file(os.path.join(subdir, file)),
                'short_url': shortURL
            }
            URL_Mapping[file] = obj

    print 'Counts'
    print count
    print len(urlMapping)
    return URL_Mapping
    # print urlMapping

if __name__ == '__main__':
    print generateShortDirectory('/Users/manishdwibedy/PycharmProjects/MIME/Data', 'HASH')
    # urlShortner('asdasdas')
