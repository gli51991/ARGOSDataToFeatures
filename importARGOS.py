##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2018
## Author: John.Fay@duke.edu (for ENV859)
##---------------------------------------------------------------------

# Import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
inputFile = 'V:/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = "V:/ARGOSTracking/Scratch/ARGOStrack.shp"

# Open the ARGOS data file for reading
inputFileObj = open(inputFile, 'r')

# Get the first line of data, so we can use a while loop
lineString = inputFileObj.readline()
while lineString:

    # Set code to run only if the line contains the string "Date: "
    if ("Date :" in lineString):
        lineData = lineString.split()
        print(lineData[0])
        break

    
    # Get the next line
    lineString = inputFileObj.readline()