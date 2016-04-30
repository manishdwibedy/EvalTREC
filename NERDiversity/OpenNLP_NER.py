import requests
import json
import os.path

def extract_NER(file_location):
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
        response = requests.put("http://localhost:9998/meta", headers=headers, data=mydata, params={'filename': headers['filename']})
        json_output = response.text


    obj = json.loads(json_output)

    NER_data = {}
    for key, value in obj.iteritems():
        key = str(key)
        if key.startswith('NER_'):
            NER_concepts = []

            for NER_concept in value:
                NER_concept = str(NER_concept)
                NER_concepts.append(NER_concept)

            NER_data[key[4:]] = NER_concepts

    return NER_data

if __name__ == "__main__":

    file_name = '/Users/manishdwibedy/PycharmProjects/MIME/Data/html/Training/0A0C0478C62A4BF29F47B5783CBD2CEB12DCF27E5BCD56A4871AFF84FB0C5DD2'
    print extract_NER(file_name)