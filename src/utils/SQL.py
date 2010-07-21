'''
Created on 2010-07-20

@author: Kelum Peirs (kelum86@gmail.com)
'''
import sqlite3 as db

class SQL(object):
    '''
    SQL Database. Wrapper for sqlite.
    '''
    _isOpen = False
    
    def __init__(self, path):
        self._path = path
        
    def connect(self):
        self._conn = db.connect(self._path)
        self._isOpen = True
    
    def close(self):
        self._conn.close()
        self._isOpen = False
    
    def commit(self):
        if self._isOpen:
            try:
                self._conn.commit()
            except db.DatabaseError:
                self._conn.rollback()
    
    def concat(self,str1, str2):
        return "%s %s" %(str1, str2)
        
    def createTable(self, name, headings, headingsType):
        if self._isOpen:
            if len(headings) != len(headingsType):
                return False
        
            decs = ",".join(["%s %s" % (headings[i], headingsType[i]) for i in range(len(headings))])
        
            stmt = "CREATE TABLE %s ( %s )" % (name, decs)
            print stmt
            cur = self._conn.cursor()
            cur.execute(stmt)
            cur.close()
            return True
        
        return False
        
        
        
        
         
        
        