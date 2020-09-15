# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:32:00 2020

@author: Arbab Ali
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 17:29:15 2020

@author: Arbab Ali
"""

import urllib.request,urllib.parse,urllib.error

import json
import ssl

api_key=42
serviceUrl='http://py4e-data.dr-chuck.net/json?'


#IGNORING THE SSL CERTIFICATE

CTX=ssl.create_default_context()
CTX.check_hostname=False
CTX.verify_mode=ssl.CERT_NONE
parms=dict()
while True:
    address=input("ENTER UNIVERSTY NAME:")
    
    if(len(address)<1): break
    
    parms['address']=address
    #parms['sensor']=False
    parms['key']=api_key
    #binding the UNIVERSTY NAME WITH SERVICE URL 
    
    url=serviceUrl+ urllib.parse.urlencode(parms)
    
    
    print("Retriving data from: ",url)
    
    
    u_handler=urllib.request.urlopen(url,context=CTX).read()
    
    data=(u_handler.decode())
    try:
        data=json.loads(data)
    except:
        data=None
    
    if not data or 'status' not in data or data['status']!='OK':
        print("==========FAILED TO RETRIEV DATA=========")
        print (data)
        break
    print(json.dumps(data,indent=2))
    
    place_id=data['results'][0]["place_id"]
    print("place id:",place_id)
    
    