# -*- coding: utf-8 -*-

'''


@author: Administrator
'''
import cx_Oracle

class DBOper():
    '''
    classdocs
    '''


    def __init__(self, conn_str=''):
        '''
        Constructor
        '''
        self.db = cx_Oracle.connect(conn_str)
     
    def getResultBySql(self, sqlstr):
        cursor = self.db.cursor()
        rt = cursor.execute(sqlstr).fetchall()
        cursor.close()
        return rt
    
    def disConnect(self):
        self.db.close()    
        