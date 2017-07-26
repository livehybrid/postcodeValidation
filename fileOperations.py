class fileOperations:
        
    def loadData(self, filePath):
        import StringIO
    
        self.openDataFile(filePath)
        importFileContentsRaw = self.readFile()
        return StringIO.StringIO(importFileContentsRaw)
        
    def openDataFile(self, filePath):
        import os.path
        import gzip
        import mimetypes

        if not os.path.exists(filePath):
            print "Input file does not exist"
            quit()

        compressionType = mimetypes.guess_type(filePath)[1]
        fileType = mimetypes.guess_type(filePath)[0]

        if compressionType == "gzip":
            loadedFile = gzip.open(filePath, 'r')

        elif compressionType == None and fileType == "text/csv":
            loadedFile = open(filePath, 'r')
        
        else:
            print "Runtime Exception - Invalid File Type"
            quit()
            
        self.fileHandle = loadedFile
        
    def openOutputFile(self, filePath):
        import os.path
        if filePath == "":
            print "Runtime Error: Filepath cannot be blank"
            quit()
        self.fileHandle = open(filePath,'w')

    def writeCSVHeader(self):
        self.fileHandle.write('row_id,postcode\n')
        
    def append(self, data):
        self.fileHandle.write(data)
        
    def appendLines(self, lines):
	    self.fileHandle.writelines(lines)
    
    def closeFile(self):
	    self.fileHandle.close();
    
    def readFile(self):
        fileContents = self.fileHandle.read()
        self.fileHandle.close()
        return fileContents