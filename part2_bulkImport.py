# coding=utf8
from postcodeValidator import postcodeValidator
from fileOperations import fileOperations

validator = postcodeValidator()
inputFile = fileOperations()
outputFile = fileOperations()

importFilePath = "import_data.csv"
failedOutputFile = "failed_validation.csv"

importFileContents = inputFile.loadData(importFilePath)
outputFile.openOutputFile(failedOutputFile)
outputFile.writeCSVHeader();

validator.validateByLine(importFileContents,outputFile.append)

outputFile.closeFile()