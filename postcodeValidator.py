import re
import StringIO
import csv
class postcodeValidator:
    

    
    regexSearch = r"((GIR\s0AA)|((([A-PR-UWYZ][0-9][0-9]?)|(([A-PR-UWYZ][A-HK-Y][0-9](?<!(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)[0-9])[0-9])|([A-PR-UWYZ][A-HK-Y](?<!AB|LL|SO)[0-9])|(WC[0-9][A-Z])|(([A-PR-UWYZ][0-9][A-HJKPSTUW])|([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY]))))\s[0-9][ABD-HJLNP-UW-Z]{2}))"
    
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
            print "Found Valid Postcode: "+match.group(0)+"\n"
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
                        print "Found Invalid Postcode: "+postcode+"\n"

    
    def sortResults(self,results):
        return sorted(results,key=lambda x: int(re.search("\d+",x).group()))