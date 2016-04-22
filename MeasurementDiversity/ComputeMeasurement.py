from util import utility
from Tika.getTika import Tika
from Solr.MIME import MIME_Core
import CalculateTagRatio

class GetMeasurementInformation(object):

    def __init__(self):
        self.SOLR = MIME_Core()

    def computeMeasurement(self):
        """
        Computation of the mime type of all the files in the solr core
        :return: the list of MimeTpye object
        """

        MeasurementList = []
        # Getting the files whose meta data would be computed
        response = MIME_Core().queryAll()
        files = response.result.dict['response']['docs']

        parsedFiles = 0
        totalFiles = len(files)
        utility.printProgress(parsedFiles, totalFiles, prefix = 'Progress:', suffix = 'Complete', barLength = 50)


        tika = Tika()
        # Looping over all the files
        for file in files:
            # Computing the language type
            filelocation = file['file'][0]

            measurements = CalculateTagRatio.computeTagRatioFile(filelocation)

            if measurements:
                file['measurements'] = measurements
            else:
                file['measurements'] = 'N.A.'

            # Appending to the list
            MeasurementList.append(file)

            parsedFiles += 1
            if parsedFiles % 30 == 0:
                utility.printProgress(parsedFiles, totalFiles, prefix = 'Progress:', suffix = 'Complete', barLength = 50)

        # Returning the list
        return MeasurementList

    def addMeasurement(self):
        measurement = self.computeMeasurement()

        self.SOLR.index(measurement)