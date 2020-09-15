# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 17:36:44 2020

@author: Arbab Ali
"""
import re
link=r'C:\Users\Arbab Ali\Desktop\WEBSCRAPINNG  WITH PYTHON\New folder\regex_sum_901941.txt'
hand=open(link)
total=0
number=list()
for line in hand:
    number=list(map(int,(re.findall('[0-9]+',line))))
    total=total+sum(number)
        
print(total)
