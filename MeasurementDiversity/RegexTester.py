import re

class MeasurementRegex():

    def __init__(self):
        """
        Creates the regex to be used to get measurements
        :return:
        """
        self.regex = r"(\d+(\.\d+)?)\s*(\w+)"

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
        :return: the tuple containing the measure and unit, if the string contains a measurement,
        otherwise None is returned
        """
        if(self.isMeasurement(string)):
            matches = re.search(self.regex, string)
            measure = matches.group(1)
            unit = matches.group(3)
            return measure, unit
        else:
            return None


if __name__ == '__main__':
    string = 'assaa asdasd cvxvxcv adsasd asddasd'
    print MeasurementRegex().isMeasurement(string)
    print MeasurementRegex().getMeasurement(string)
