# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:38:30 2020

@author: Arbab Ali
"""

import xml.etree.ElementTree as ET


data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

data2 = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''
tree=ET.fromstring(data)
print('Name:',tree.find('name').text)
print("Attr:",tree.find('email').get('hide'))
#lst1=tree.findall('person')

#print(lst1)
tree2=ET.fromstring(data2)

lstt=tree2.findall('users/user')
#print(lstt)
print("users:",len(lstt))

for tag in lstt:
    print('name',tag.find('name').text)
    print('Id:',tag.find('id').text)
    print('attribute',tag.get('x'))

