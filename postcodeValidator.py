import re
import StringIO
import csv
class postcodeValidator:
    

    
    regexSearch = r"(([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2}))"
    
    # Param: postcode - String - The postcode you intend to check the validity of
    # The function prints text to stdout to declare the validity of the input postcode
    def validatePostcode(self,postcode):
        
        matches = re.search(self.regexSearch, postcode)
        if matches and matches.group(0)==postcode:
            return True
        else:
            return False
    
    def validateMultiLines(self,lines):
        passedList = []
        for match in re.finditer("([0-9]+\,)"+self.regexSearch, lines.getvalue()):
            passedList.append(match.group(0)+"\n")
        return passedList
        
    def outputValidity(self,postcode):
        validPostcode = self.validatePostcode(postcode)
        if validPostcode:
            print ("{postcode} - Valid".format(postcode=postcode))
        else:
            print ("{postcode} - InValid".format(postcode=postcode))
    
    def validateByLine(self,inputLines,outputFunction):

        for validationLine in inputLines:
            reader = csv.reader(StringIO.StringIO(validationLine), delimiter=',')
            for row in reader:
                rowId = row[0]
                postcode = row[1]
                if rowId != "row_id": #Ignore the header row
                    if self.validatePostcode(postcode) == False:
                        outputFunction(rowId+","+postcode+"\n")

    
    def sortResults(self,results):
        return sorted(results,key=lambda x: int(re.search("\d+",x).group()))