"""
The Text-To-Tag Ratio (TTR) is the basis by which we analyze a Web page in preparation for clustering.
"""

from bs4 import BeautifulSoup
import numpy
import requests
import os

url = 'http://localhost:9998/tika'

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

    return TTRArray

def calculateTTRMean(TRRArray):
    sum = 0
    for TRRValue in TRRArray:
        sum += TRRValue

    return sum/len(TRRArray)

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
    TRRArray = calculateFileTagRatio(filename)
    print calculateTTRMean(TRRArray)

    print TRRArray
    print len(TRRArray)

    smoothedArray = smooteTRRArray(TRRArray)
    print smoothedArray
    print len(smoothedArray)

    mean = numpy.std(smoothedArray)
    print mean

    meanArray = [mean] * len(smoothedArray)
    print meanArray