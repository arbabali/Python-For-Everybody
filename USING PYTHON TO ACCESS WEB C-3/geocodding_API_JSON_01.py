# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 17:29:15 2020

@author: Arbab Ali
"""

import urllib.request,urllib.parse,urllib.error

import json
import ssl

#api_key="AIzaSyBH86SYWkse6z27sVpZWWLpx9Bzd3YSP10"
api_key=False
if api_key is False:
    api_key="AIzaSyBH86SYWkse6z27sVpZWWLpx9Bzd3YSP10"
    serviceUrl="http://py4e-data.dr-chuck.net/json?"
else:
    serviceUrl='https://maps.googleapis.com/maps/api/geocode/json?'
    
#IGNORING THE SSL CERTIFICATE ERROR
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
    
while True:
    address=input("Enter Location:")
    if len(address)>1:break

    parms=dict()
    parms['sensor']=False 
    parms['address']=address  
    
    if api_key is not False :
        parms['Key']=api_key
        
    url=serviceUrl+urllib.parse.urlencode(parms)
    
    print("Retrieveing..",url)
    
    u_handler=urllib.request.urlopen(url,context=ctx).read()
    
    data=u_handler.decode()
    
    print("Retrieved data :",len(data),"charachters")
    
    
    try:
        js=json.loads(data)
    except:
        js=None
        
    
    if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            
    
    print (json.dumps(js,indent=4))