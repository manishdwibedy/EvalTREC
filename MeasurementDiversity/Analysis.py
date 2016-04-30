from util import utility
from Solr.MIME import MIME_Core
from collections import defaultdict
import csv

class MeasurementAnalysis(object):
    def __init__(self):
        self.SOLR = MIME_Core()

    def getMeasurements(self):
        """
        Getting the measurements from the solr instance, if the files had any measurement information
        :return: the list of files
        """

        MeasurementList = []
        # Getting the files whose meta data would be computed
        response = MIME_Core().queryAll("-measurements:N.A. measurements:['' TO *]", 'measurements')
        files = response.result.dict['response']['docs']

        return files

    def getUniqueUnits(self):

        files = self.getMeasurements()

        index = 0
        total = len(files)

        utility.printProgress(index, total)

        measurement_units = defaultdict(list)

        for file in files:
            file_measurements = file['measurements']
            for line_measurement in file_measurements:
                measurements = line_measurement.strip().split(';;')
                for measurement in measurements:
                    measurement_data = measurement.strip().split('<<>>')
                    if len(measurement_data) == 2:
                        unit = measurement_data[1]
                        measure = measurement_data[0]
                        measurement_units[unit] = measure
            index+=1
            utility.printProgress(index, total)
        return measurement_units

    def outputUniqueUnits(self, measurement_units):
        with open('test1.txt', 'wb') as testfile:
            for unit, measures in measurement_units.iteritems():
                output =  '%(unit)s;%(measures)s\n' % {"unit": unit, "measures": measures}
                testfile.write(output)
                # print 'Unit is : ', unit
                # print 'Found measures like %(measures)s.' % {"measures": measures}
                # print 'Found measures like : ' ','.join(measures)
            pass


        # with open('test1.csv', 'wb') as testfile:
        # csv_writer = csv.writer(testfile)
        # for unit, measures in measurement_units.iteritems():
        # for y in range(length):
        #     csv_writer.writerow([x[y] for x in hello])

if __name__ == '__main__':
    analysis = MeasurementAnalysis()
    measurement_units = analysis.getUniqueUnits()

    analysis.outputUniqueUnits(measurement_units)