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

                            try:
                                quantity = float(data[0].strip())
                            except ValueError:
                                continue
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
                                    'sum': quantity
                                }
                                measurement_json[unit] = data
                                pass
                        # Check if multiple quantities in the line
                        if ';;' in line:
                            data = line.split(';;')
                            for measurement in data:
                                data = measurement.split('<<>>')
                                quantity = float(data[0].strip())
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
                                        'min': float(quantity),
                                        'max': float(quantity),
                                        'count' : 1,
                                        'sum': float(quantity)
                                    }
                                    measurement_json[unit] = data
                                    pass

                else:
                    # No measurement data
                    pass
            measurements_diveristy[mime] = measurement_json

            final_output = {}
            for unit, unit_data in measurement_json.iteritems():
                try:
                    data = {
                        'min': unit_data['min'],
                        'max': unit_data['max'],
                        'mean': float(unit_data['sum']) / float(unit_data['count'])
                    }
                    final_output[unit] = data
                except:
                    # print unit_data
                    pass

            output = {}
            unitList = []
            minList = []
            maxList = []
            meanList = []
            for unit, unit_info in final_output.iteritems():

                if unit_info['min'] > utility.constant.MAX_MEASURE or unit_info['max'] > utility.constant.MAX_MEASURE or unit_info['mean'] > utility.constant.MAX_MEASURE:
                    continue
                unitList.append(unit)
                minList.append(unit_info['min'])
                maxList.append(unit_info['max'])
                meanList.append(unit_info['mean'])
            print 'The non units are :'
            print non_units

            output = {
                'min': minList,
                'max' :maxList,
                'mean' :meanList
            }


            out_file = open('data/measure/'+mime[mime.index('/')+1:]+'.json',"w")
            json.dump(output,out_file, indent=4)

            out_file = open('data/units/'+mime[mime.index('/')+1:]+'_units.json',"w")
            json.dump(unitList,out_file, indent=4)

            pass
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