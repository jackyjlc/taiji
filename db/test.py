#-*- coding: utf-8#
'''
Created on 2018��2��24��

@author: Administrator
'''

#print('hello world!!!')

import oper.XmlOper
from db.DBOper import DBOper


def helloproc():
    print('hello world!!!')
    
def printXml():
    dblist = []
    fileName = r'f:\\temp\\dblist.xml' 
    obj = oper.XmlOper.XmlOper()
    dom = obj.readXml(fileName)

    for db in dom.iter('db'):
        uid = db.find('uid').text
        pwd = db.find('pwd').text
        host = db.find('host').text
        port = db.find('port').text
        sid = db.find('sid').text 
        
        conn_str = '%s/%s@%s:%s/%s' %(uid,pwd,host,port,sid)
        dblist.append(conn_str)
        
    for s in dblist:
        print('数据库连接字符串：%s' %(s))

        
        '''
        for node in db.getchildren():
            print('nodeName: %s, nodeValue: %s' %(node.nodeName, node.nodeValue))
    
    
    '''
        '''
    print(len(bb))
    print(bb[0].firstChild.data)
    print(root.nodeName)
    '''   
def testdb():
    j = 0
    conn_str = 'jk/jk@localhost:1521/orcl' 
    sql = 'select * from t_test1 where rownum<9' 
    db = DBOper(conn_str)  
    rt = db.getResultBySql(sql)
    while j<len(rt):
        print(rt[j][1])
        j += 1
    db.disConnect()        

if __name__ == '__main__':
    testdb()
#    helloproc()