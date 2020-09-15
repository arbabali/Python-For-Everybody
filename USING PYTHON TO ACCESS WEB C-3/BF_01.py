# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:37:53 2020

@author: Arbab Ali
"""

import urllib 
from urllib import request 
from bs4 import BeautifulSoup 


hand=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_901943.html')

soup=BeautifulSoup(hand,'html.parser')
soup=soup('span')
total=0
for line in soup:
    total+=int(line.string)
    
print(total)