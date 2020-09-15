# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 17:54:34 2020

@author: Arbab Ali
"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl

#api_key = "AIzaSyC3iku9duUwRPgYeHKjaMq-B917fAFhr3Q"
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro
api_key=False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(js, indent=4))
    file=open('Address.txt','w')
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    file.write("lat: "+ str(lat))
    file.write(" lang: " +str(lng))
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    file.write(" "+str(location))
    file.close()
