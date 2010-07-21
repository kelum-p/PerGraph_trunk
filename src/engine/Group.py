#Created on 2010-06-15
#@author: Kelum Peiris (kelum86@gmail.com)

from parsers.CSVParser import CSVParser
from utils.SQL import SQL

class Group(object):
    # Represent a group of data
    # Groups can be compared to eachother
    # Groups try to combine common data stores in more than 1 data file
    
    _headings = []
    _headingsType = []
    _currRow = 0
        
    def __init__(self, name, fileTypes):
        self._name = name
        self._fileTypes = fileTypes
        
       
    # @param filenameList: List of filenames that contains data.
    # @summary: 
    #    Uses the file parsers to parse each data file and combine common data
    def createGroup(self, filenameList):
                
        # Get all the possible headers in the files
        for filename in filenameList:
            if filename.endswith('.csv'):
                self._parser = CSVParser(filename)
            
            self._parser.parse()
            for heading in self._parser.getHeadings():
                if self._headings.count(heading) == 0:
                    self._headings.append(heading)
                    self._headingsType.append(self._parser.getHeadingType(heading))
            
        
        db = SQL("C:\\PerGraph\\" + self._name + ".db")
        db.connect()
        db.createTable("data",self._headings, self._headingsType)
        db.commit()
        db.close()
       
        
                
                
            
            
    
    def sort(self, heading):
        print 'BEFORE'
        for item in self._allData:
            print item
        
        try:
            idx = self._headings.index(heading)
            self._allData.sort(lambda x, y: cmp(x[idx], y[idx]))
        except ValueError:
            print 'Header %s does not exist' % heading
            
        print 'AFTER'
        for item in self._allData:
            print item
                        
                        
                        
                
                
        
        
            
            
            
        
        
            
                
            
                 
            
        
        
        
