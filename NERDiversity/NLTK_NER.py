import requests
import json
import os.path
from util import utility
from Solr.MIME import MIME_Core

class ExtractNER(object):

    def __init__(self):
        self.SOLR = MIME_Core()
        self.url = "http://localhost:9998/meta"

    def extractNERBulk(self):
        """
        Computation of the mime type of all the files in the solr core
        :return: the list of MimeTpye object
        """

        NER_List = []

        # Getting the files where NLTK computation has not been done
        response = MIME_Core().queryAll('-NLTK:* OR -NLTK_NAMES:*')
        files = response.result.dict['response']['docs']

        fileIndex = 0
        totalFiles = len(files)

        print 'Adding metadata to the dataset'
        utility.printProgress(fileIndex, totalFiles, prefix = 'Progress:', suffix = 'Complete', barLength = 50)

        # foundNER = False

        # Looping over all the files
        for file in files:
            # Computing the NER using Open NLP
            NER = self.extract_NER(file['file'][0])

            # Found NER
            if len(NER) > 0:
                # foundNER = True
                for NERclass, NER_wordList in NER.iteritems():
                    file['NLTK_'+NERclass] = NER_wordList
            else:
                file['NLTK'] = ['N.A.']

            # Appending to the list
            NER_List.append(file)

            fileIndex += 1
            utility.printProgress(fileIndex, totalFiles, prefix = 'Progress:', suffix = 'Complete', barLength = 50)

            # if foundNER:
            if len(NER_List) % 1000 == 0:
                self.SOLR.index(NER_List)
                NER_List = []
        # Returning the list
        return NER_List

    def addNER(self):
        NER = self.extractNERBulk()

        print '\n\nStarting to index the NER of the files'
        self.SOLR.index(NER)
        print '\nIndexed!'


    def extract_NER(self, file_location):
        '''
        Getting the NER concepts of a single file
        :param file_location: the absolute file name of the file
        :return: the NER object
        '''

        file_name = os.path.basename(file_location)
        headers = {
                    'Content-Disposition': 'attachment',
                    'filename': file_name,
                    'Accept': 'application/json'
                  }

        with open(file_location) as fh:
            mydata = fh.read()
            response = requests.put(self.url, headers=headers, data=mydata,
                                    params={'filename': headers['filename']})
            json_output = response.text

        NER_data = {}
        try:
            obj = json.loads(json_output)

            for key, value in obj.iteritems():
                key = str(key)
                if key.startswith('NER_'):
                    NER_concepts = []

                    for NER_concept in value:
                        NER_concept = str(NER_concept)
                        NER_concepts.append(NER_concept)

                    NER_data[key[4:]] = NER_concepts
        except ValueError:
            pass
        return NER_data

if __name__ == "__main__":

    ner = ExtractNER()
    ner.addNER()
