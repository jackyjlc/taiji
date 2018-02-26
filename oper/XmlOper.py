#-*- coding: utf-8
'''
Created on 2018-2-26

@author: LongChunJiang
'''

#import xml.dom.minidom
from xml.etree import ElementTree as ET

class XmlOper:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        
    def readXml(self,fileName):
        dom = ET.parse(fileName)
        return dom
            