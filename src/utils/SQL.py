'''
Created on 2010-07-20

@author: Kelum Peirs (kelum86@gmail.com)
'''
import sqlite3 as db

class SQL(object):
    '''
    SQL Database. Wrapper for sqlite.
    '''
    
    def __init__(self, path):
        self._path = path
        
    def connect(self):
        self._conn = db.connect(self._path)
    
    def close(self):
        self._conn.close()
    
    def commit(self):
        try:
            self._conn.commit()
        except db.DatabaseError:
            self._conn.rollback()
        
    def createTable(self,headings):
        headings_str = ','.join([heading for heading in headings])
        
        
        
         
        
        