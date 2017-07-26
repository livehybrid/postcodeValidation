# coding=utf8
from postcodeValidator import postcodeValidator
from fileOperations import fileOperations
import re

validator = postcodeValidator()
inputFile = fileOperations()
passedFile = fileOperations()
failedFile = fileOperations()

importFilePath = "import_data.csv"
failedOutputFile = "failed_validation.csv"
passedOutputFile = "passed_validation.csv"

print "Loading input file"
importFileContents = inputFile.loadData(importFilePath)

print "Creating output files"
passedFile.openOutputFile(passedOutputFile)
passedFile.writeCSVHeader();
failedFile.openOutputFile(failedOutputFile)
failedFile.writeCSVHeader();

fullList = []

print "Processing file"
for validationLine in importFileContents:
    if validationLine != "row_id,postcode\n": fullList.append(validationLine)

passedList = validator.validateMultiLines(importFileContents)

print "Compiling failed test results"

passedListSet = set(passedList)

failedList = [line for line in fullList if line not in passedListSet]

failedList = validator.sortResults(failedList)
passedList = validator.sortResults(passedList)

print "Writing results to files"
passedFile.appendLines(["%s" % passedRow  for passedRow in passedList])
failedFile.appendLines(["%s" % failedRow  for failedRow in failedList])

passedFile.closeFile()
failedFile.closeFile()

print "Finished"