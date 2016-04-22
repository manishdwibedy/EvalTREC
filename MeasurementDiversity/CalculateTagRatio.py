"""
The Text-To-Tag Ratio (TTR) is the basis by which we analyze a Web page in preparation for clustering.
"""

from bs4 import BeautifulSoup
import numpy
import requests
import HTMLParser
import RegexTester
url = 'http://localhost:9998/tika'


import re
def striphtml(string):
    """
    Remove HTML tags and decode HTML character
    :param string: HTML string
    :return: string, tags removed
    """
    p = re.compile(r'<.*?>')
    string = p.sub('', string)
    h= HTMLParser.HTMLParser()
    string =  h.unescape(string)
    return string

def calculateLineTagRatio(line):
    """
    Calculation of the line's tag ratio.
    :param line: the line containing HTML data
    :return: the text-to-tag ratio is returned
    """

    soup = BeautifulSoup(line, "html.parser")

    tags = []
    non_tag_data = ""

    # Would loop through all the children of the HTML text
    for tag in soup.findChildren():

        # Would append the tag to the tags list
        tags.append(tag.name)

        # If the tag has content as an immediate descentent, add to the non tag data
        if len(tag.contents) == 1:
            # child is HML content
            if isinstance(tag.contents[0], basestring):
                non_tag_data += tag.contents[0]

    # Compute the number of tags seen
    tag_count = len(tags)

    # Computation of TTR for the line
    if tag_count == 0:
        return len(non_tag_data)
    else:
        return len(non_tag_data) / tag_count

# Using this current file
filename = "/Users/manishdwibedy/Downloads/usc_team_breakout__sp2016_.xlsx"


def stripHTMLdata(filename):
    """
    Stripping all the irrelevant data like script tags, comments and empty lines
    :param filename: the absolute path to strip its HTML representation of irrelevant tags
    :return: the stripped HTML data in the form of a list
    """

    # Getting the HTML data for the file
    # and then splitting the data by newline character
    HTMLdata = generateHTML(filename).split('\n')

    strippedHTMLdata = []

    # For each line in the HTML data
    for line in HTMLdata:

        # convert to the ASCII, ignoring characters that can't be encoded
        sLine = line.encode('ascii','ignore')

        # Ignoring tags like script, comment tags and empty lines,
        # Else, add them to the list
        if sLine.find("<script") == -1 and sLine.find('<!--') == -1 and len(sLine.strip()) > 0:
            strippedHTMLdata.append(sLine)

    return strippedHTMLdata


def calculateFileTagRatio(filename):
    """
    Calculating the file's Text-to-Tag ratio
    :param filename: the absolute path of the file
    :return: an array where each line's TTR is present
    """
    TTRArray = []

    strippedHTMLdata = stripHTMLdata(filename)
    for line in strippedHTMLdata:
        TTRArray.append(calculateLineTagRatio(line))

    return strippedHTMLdata, TTRArray

def calculateTTRMean(TRRArray):
    sum = 0
    for TRRValue in TRRArray:
        sum += TRRValue

    total = len(TRRArray)
    if total != 0:
        return sum/total
    else:
        return 0

def smooteTRRArray(TRRArray):
    """
    This method would smoothe the TRR Array
    :param TRRArray: The TRR Array to be smoothed
    :return: The smoothed array
    """

    # Using this as the radius
    radius = 2

    # Final smoothed TRR Array
    smoothedTRRArray = []

    for smoote_index in range(0, len(TRRArray)):
        # Sum of nearby elements
        nearby_values = get_nearby_values(TRRArray, smoote_index, radius)

        # Use this sum as the smoothed value
        smoothedTRRArray.append(nearby_values)

    return smoothedTRRArray

def get_nearby_values(TRRArray, index, radius):
    """
    Getting the nearby values
    :param TRRArray: The TRR Array
    :param index: The index of the current value
    :param radius: The radius to define 'nearby' values
    :return: The sum of nearby values
    """

    # get the start index
    if index - radius >= 0:
        start_index = index - radius
    else:
        start_index = 0

    # get the end index
    if index + radius <  len(TRRArray):
        end_index = index + radius
    else:
        end_index = len(TRRArray) - 1

    sum = 0

    # Need to consider index from start_index to end_index, both inclusive
    for loop_index in range(start_index, end_index + 1):
        sum += TRRArray[loop_index]

    return sum

def generateHTML(filename):
    """
    This method would generate the HTML equivalent of the file being passed.
    :param filename: the absolute path of the file being converted
    :return: The HTML representation of the file
    """

    # The header foces the html representation
    headers = {'Accept': 'text/html'}

    # Opening the said file as uploading the file to the URL
    with open(filename, 'rb') as file:
        # Getting the response back from the local server
        response = requests.put(url, data=file, headers=headers)

    # Return the HTML string
    return response.text

def computeTagRatioFile(filename):
    HTMLdata, TRRArray = calculateFileTagRatio(filename)
    mean =  calculateTTRMean(TRRArray)

    smoothedArray = TRRArray
    # smoothedArray = smooteTRRArray(TRRArray)

    std = numpy.std(smoothedArray)

    contentData = []
    for index in range(0, len(smoothedArray) ):
        if smoothedArray[index] > mean:
            contentData.append(striphtml(HTMLdata[index]))


    if len(contentData) > 0:
        return extractMeasurement(contentData)
    else:
        return None

def extractMeasurement(contentData):
    indexes = []
    measurement = RegexTester.MeasurementRegex()
    for line in contentData:
        measurementData = measurement.getMeasurement(line)
        if measurementData:
            indexes.append(measurementData)
    return indexes



def num_there(string):
    for char in string:
        if char.isdigit():
            return True
    return False
    # return any(i.isdigit() for i in s)

if __name__ == '__main__':
    filename = '/Users/manishdwibedy/PycharmProjects/MIME/final/atom+xml/D5EE01268FEB9E28ED7AEFF1B8D379C9E89B9B3D410EBE271133D01A3BE9F9AB'
    # computeTagRatioFile(filename)
