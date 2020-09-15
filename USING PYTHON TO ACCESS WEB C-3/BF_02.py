# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:52:11 2020

@author: Arbab Ali
"""

import urllib 
from urllib import request 
from bs4 import BeautifulSoup 

link='http://py4e-data.dr-chuck.net/known_by_Zaineddine.html'

hand=urllib.request.urlopen(link).read()
count=int(input("ETNER THE COUNT:"))
position=int(input("ENTER THE POS:"))
hand=urllib.request.urlopen(link).read()
soup=BeautifulSoup(hand,'html.parser')  
tags=soup('a')
while(count>0):
    #print(soup.prettify())
    url=(tags[position-1].get('href',None))
    hand2=urllib.request.urlopen(url).read()
    soup2=BeautifulSoup(hand2,'html.parser')
    tags=soup2('a')
    #print(url)
    count-=1
    
print(url)