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

        final_output = {}

        non_units = set()
        for mime in mimeList:
            measurement_json = {}
            print mime[mime.index('/')+1:]
            query = 'metadata:%s' % (mime)
            if 'html' in mime:
                response = MIME_Core().queryAll(query=query, rows=13000)
            else:
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



        unitList = {}
        minList = {}
        maxList = {}
        meanList = {}

        for mime, mime_unit_data in measurements_diveristy.iteritems():
            for unit, unit_data in mime_unit_data.iteritems():
                if unit_data['max'] > 1000000:
                            continue

                try:
                    unitList[unit.lower()] = 1

                    if unit.lower() in maxList:
                        if unit_data['max'] < minList[unit]:
                            maxList[unit.lower()] = unit_data['max']

                    else:
                        maxList[unit.lower()] = unit_data['max']
                        pass


                    if unit.lower() in minList:
                        if unit_data['min'] < minList[unit]:
                            minList[unit.lower()] = unit_data['min']

                    else:
                        minList[unit.lower()] = unit_data['min']
                        pass


                    if unit.lower() in meanList:
                        meanList[unit.lower()] = ((unit_data['sum'] / unit_data['count']) + meanList[unit.lower()]) / 2
                    else:
                        meanList[unit.lower()] = unit_data['sum'] / unit_data['count']


                except:
                    # print unit_data
                    pass

        output = {}

        min_list = []
        for unit, value in minList.iteritems():
            min_list.append(value)

        max_list = []
        for unit, value in maxList.iteritems():
            max_list.append(value)

        mean_list = []
        for unit, value in meanList.iteritems():
            mean_list.append(value)

        unit_list = []
        for unit, value in unitList.iteritems():
            unit_list.append(unit)

        obj = {
            'min': min_list,
            'max': max_list,
            'mean': mean_list
        }
        out_file = open('data/overall/output.json',"w")
        json.dump(obj,out_file, indent=4)

        out_file = open('data/overall/output_units.json',"w")
        json.dump(unit_list,out_file, indent=4)

        pass

    def getType(self, unit):
        unit_tree = {
                'time': ['mintues','years','day', 'hours', 'months'],
                'length': ['meter','miles','meters','kilometer', 'kilometers','inch','ft', 'km', 'm'],
                'memory': ['bytes','GB','Mb'],
                'area': ['sq km', 'square meters', 'hectares']
            }
        for type, mimeList in unit_tree.iteritems():
            if unit.lower() in mimeList:
                return type
        return None

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