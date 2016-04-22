import re

class MeasurementRegex():

    def __init__(self):
        """
        Creates the regex to be used to get measurements
        :return:
        """
        self.regex = r"(\d+(\.\d+)?)(\s*([a-zA-Z]+))(\s*(\w[a-zA-Z]+))?"

    def isMeasurement(self, string):
        """
        Checks whether the string contains a measurement or not
        :param string: the string to be checked
        :return: True if a measurement is found, else False
        """

        match = re.search(self.regex, string)
        if match:
            return True
        else:
            return False


    def getMeasurement(self, string):
        """
        Gets the measurement from the string
        :param string: the string to be search
        :return: the list of object containing the measure and unit, if the string contains a measurement,
        otherwise None is returned
        """
        measurementList = []

        if(self.isMeasurement(string)):
            matches = re.findall(self.regex, string)
            for match in matches:
                if not match[2].isdigit():
                    pass
                if len(match) == 6:
                    measure = {
                        'measure': match[0],
                        'unit': match[3] + ' ' + match[5]
                    }
                else:
                    measure = {
                        'measure': match[0],
                        'unit': match[3]
                    }
                measurementList.append(measure)
            return measurementList
        else:
            return None


if __name__ == '__main__':
    string = 'Steve Bloom reporting from 2014AG asd 10 M asd11 asd '
    print MeasurementRegex().isMeasurement(string)
    print MeasurementRegex().getMeasurement(string)
