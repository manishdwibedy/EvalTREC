from util import utility
from Solr.MIME import MIME_Core
import json

class Visulization(object):

    def __init__(self):
        self.SOLR = MIME_Core()
        self.units = set(utility.constant.UNITS)

    def extractMeasurements(self):
        FileSizeList = []

        # Getting the files whose size would be computed
        response = MIME_Core().facetQuery('metadata')
        mimeTypeResponse = response.result.dict['facet_counts']['facet_fields']['metadata']

        mimeList = []
        for mime_type, count in mimeTypeResponse.iteritems():
            mimeList.append(mime_type)


        measurements_diveristy = {}

        non_units = set()
        for mime in mimeList:
            measurement_json = {}
            print mime[mime.index('/')+1:]
            query = 'metadata:%s' % (mime)
            response = MIME_Core().queryAll(query=query)
            files = response.result.dict['response']['docs']
            for file in files:
                if 'measurements' not in file:
                    continue
                measurements = file['measurements']

                if measurements[0] != 'N.A.':
                    # Check for multiple lines
                    for line in measurements:
                        # Check if one quantity in the line
                        if ';;' not in line:
                            data = line.split('<<>>')
                            quantity = data[0].strip()
                            try:
                                unit = data[1].strip()
                            except IndexError:
                                continue

                            cleaned_unit = self.validateUnit(unit)
                            if 'km' == unit:
                                self.validateUnit(unit)
                            if not cleaned_unit:
                                non_units.add(unit)
                                continue

                            if unit in measurement_json:
                                old_data = measurement_json[unit]
                                if quantity > old_data['max']:
                                    old_data['max'] = quantity
                                if quantity < old_data['min']:
                                    old_data['min'] = quantity
                                old_data['count'] += old_data['count'] + 1
                                old_data['sum'] += old_data['sum'] + float(quantity)
                                pass
                            else:
                                data = {
                                    'min': quantity,
                                    'max': quantity,
                                    'count' : 1,
                                    'sum': float(quantity)
                                }
                                measurement_json[unit] = data
                                pass
                        # Check if multiple quantities in the line
                        if ';;' in line:
                            data = line.split(';;')
                            for measurement in data:
                                data = measurement.split('<<>>')
                                quantity = data[0].strip()
                                unit = data[1].strip()


                                if unit not in utility.constant.UNITS:
                                    continue
                                if unit in measurement_json:
                                    old_data = measurement_json[unit]
                                    if quantity > old_data['max']:
                                        old_data['max'] = quantity
                                    if quantity < old_data['min']:
                                        old_data['min'] = quantity
                                    old_data['count'] += old_data['count'] + 1
                                    old_data['sum'] += old_data['sum'] + float(quantity)
                                    pass
                                else:
                                    data = {
                                        'min': quantity,
                                        'max': quantity,
                                        'count' : 1,
                                        'sum': float(quantity)
                                    }
                                    measurement_json[unit] = data
                                    pass

                else:
                    # No measurement data
                    pass
            measurements_diveristy[mime] = measurement_json
            print non_units

            out_file = open('data/'+mime[mime.index('/')+1:]+'.json',"w")

            json.dump(measurement_json,out_file, indent=4)

    def validateUnit(self, unit):

        unitMap = {}
        for file_unit in self.units:
            # Matched the unit
            if unit.lower() in file_unit :
                unitMap[unit] = file_unit
                return file_unit
        return None
if __name__ == '__main__':
    Visulization().extractMeasurements()