# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:54:26 2020

@author: Arbab Ali
"""

import urllib
from urllib import request
import xml.etree.ElementTree as ET



link="http://py4e-data.dr-chuck.net/comments_901945.xml"

hand=urllib.request.urlopen(link).read()
print("retrieved Charachter Data:",len(hand))
tree=ET.fromstring(hand)
listt=tree.findall('.//count')
count=len(listt)
summ=0
for tag in listt:
    summ+=int(tag.text)
    
    
print("count:",count)
print("sum:",summ)