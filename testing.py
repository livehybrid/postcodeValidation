# coding=utf8
import unittest
from postcodeValidator import postcodeValidator
from fileOperations import fileOperations
import StringIO
import sys


class postcodeValidationTesting(unittest.TestCase):
 
    def setUp(self):
        self.validator = postcodeValidator()
        self.fileOperations = fileOperations()
    
    def testMultiLineValidationPass(self):
	    # Test list of postcodes (as loaded via file) - Expect 2 to return
        result = self.validator.validateMultiLines(StringIO.StringIO(["1,EC1A 1BB","2,W1A 0AX"]))
        #print result
        if result == ['1,EC1A 1BB\n', '2,W1A 0AX\n']: assert True
        else: assert False

    def testMultiLineValidationFail(self):
	    # Test list of postcodes (as loaded via file) - Expect 0 to return
        result = self.validator.validateMultiLines(StringIO.StringIO(["1,XX XXX","2,X1A 9BB"]))
        #print result
        if result == []: assert True
        else: assert False
        
    def testMultiLineValidationMix(self):
	    # Test list of postcodes (as loaded via file) - Expect 1 to return
        result = self.validator.validateMultiLines(StringIO.StringIO(["1,EC1A 1BB","2,X1A 9BB"]))
        #print result
        if result == ['1,EC1A 1BB\n']: assert True
        else: assert False
    
    def testOutputValidity(self):
        self.validator.outputValidity("EC1A 1BB")
        output = sys.stdout.getvalue()
        if output == "EC1A 1BB - Valid\n": assert True
        else: assert False

    def testValidateByLine(self):
        self.validator.validateByLine((["1,EC1A 1BB","2,X1A 9BB"]),sys.stdout.write)
        output = sys.stdout.getvalue()
        #print output
        if output == "2,X1A 9BB\n": assert True
        else: assert False
    
    def testValidPostcodes(self):
        # Test Postcodes that should always Pass
        assert self.validator.validatePostcode("EC1A 1BB") == True
        assert self.validator.validatePostcode("W1A 0AX") == True
        assert self.validator.validatePostcode("M1 1AE") == True
        assert self.validator.validatePostcode("B33 8TH") == True
        assert self.validator.validatePostcode("CR2 6XH") == True
        assert self.validator.validatePostcode("DN55 1PT") == True
        assert self.validator.validatePostcode("GIR 0AA") == True
        assert self.validator.validatePostcode("SO10 9AA") == True
        assert self.validator.validatePostcode("FY9 9AA") == True
        assert self.validator.validatePostcode("WC1A 9AA") == True
 
    def testInValidPostcodes(self):
        # Test Postcodes that should always Fail
        assert self.validator.validatePostcode("$%± ()()") == False
        assert self.validator.validatePostcode("XX XXX") == False
        assert self.validator.validatePostcode("A1 9A") == False
        assert self.validator.validatePostcode("LS44PL") == False
        assert self.validator.validatePostcode("Q1A 9AA") == False
        assert self.validator.validatePostcode("V1A 9AA") == False
        assert self.validator.validatePostcode("X1A 9BB") == False
        assert self.validator.validatePostcode("LI10 3QP") == False
        assert self.validator.validatePostcode("LJ10 3QP") == False
        assert self.validator.validatePostcode("LZ10 3QP") == False
        assert self.validator.validatePostcode("A9Q 9AA") == False
        assert self.validator.validatePostcode("AA9C 9AA") == False
        assert self.validator.validatePostcode("FY10 4PL") == False
        assert self.validator.validatePostcode("SO1 4QQ") == False

    def testLoadCSVFile(self):
        csvData = self.fileOperations.loadData('test_data.csv')
        if csvData.len == 160: assert True
        else: assert False
    
    def testLoadGZFile(self):
        csvData = self.fileOperations.loadData('test_data.csv.gz')
        if csvData.len == 160: assert True
        else: assert False
        
    def testOutputFile(self):
        self.outputFile = fileOperations()
        self.outputFile.openOutputFile('test_output.csv')
        self.outputFile.writeCSVHeader()
        self.outputFile.closeFile()
        assert True #Script would die if did not get to this point

        testOutputFileContents = self.fileOperations.loadData('test_output.csv')
        if testOutputFileContents.getvalue() == "row_id,postcode\n": assert True
        else: assert False

    def testOutputLine(self):
        self.outputFile = fileOperations()
        self.outputFile.openOutputFile('test_output.csv')
        self.outputFile.append("UnitTesting")
        self.outputFile.closeFile()
        testOutputFileContents = self.fileOperations.loadData('test_output.csv')
        if testOutputFileContents.getvalue() == "UnitTesting": assert True
        else: assert False
    
    def testOutputMultiLines(self):
        self.outputFile = fileOperations()
        self.outputFile.openOutputFile('test_output.csv')
        self.outputFile.appendLines(["UnitTesting1\n","UnitTesting2\n"])
        self.outputFile.closeFile()
        testOutputFileContents = self.fileOperations.loadData('test_output.csv')
        if testOutputFileContents.getvalue() == "UnitTesting1\nUnitTesting2\n": assert True
        else: assert False
        
    def testSortResults(self):
        sortedList = self.validator.sortResults(['41,OL3 5HL','5,HD4 6UL','12, WF3 1PP'])
        if sortedList == ['5,HD4 6UL', '12, WF3 1PP', '41,OL3 5HL']: assert True
        else: assert False
    

if __name__ == "__main__":
    unittest.main() # run all tests
    