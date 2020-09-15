# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:19:59 2020

@author: Arbab Ali
"""

import urllib.request,urllib.parse,urllib.error

import json




link='http://py4e-data.dr-chuck.net/comments_901946.json'

u_handler=urllib.request.urlopen(link)

json_data=json.load(u_handler)
#print(json.dumps(json_data,indent=4))
total=0
for item in json_data['comments']:
    total+=int(item['count'])
    
print(total)