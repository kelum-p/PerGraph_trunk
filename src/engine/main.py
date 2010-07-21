#Created on 2010-06-15
#@author: Kelum Peiris (kelum86@gmail.com)

from parsers.CSVParser import CSVParser
from engine.Group import Group

def main():
    print 'Welcome to Performance Graph.. software testing made easier';
    
    #p = CSVParser("J:\\My Dropbox\\Open Source Projects\\MKS_Data\\results44494_001\\ops\\QA-FARMF.1.user1.timings.csv");
    #p.parse()
    #headings = p.getHeadings()
    #data = p.getData(headings[0]);
    #print data
    #data = p.getData(headings[2]);
    #print data
    
    g = Group('yarg', 'CSV');
    filenames = ["J:\\My Dropbox\\Open Source Projects\\MKS_Data\\results44494_001\\ops\\QA-FARMF.1.user1.timings.csv",
                 "J:\\My Dropbox\\Open Source Projects\\MKS_Data\\results44494_001\\ops\\QA-FARMF.2.user2.timings.csv"]
    g.createGroup(filenames)
    g.sort('Timestamp')

if __name__ == '__main__':
    main()