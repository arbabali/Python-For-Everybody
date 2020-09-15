# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:01:18 2020

@author: Arbab Ali
"""

import socket

my_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


my_sock.connect(("data.pr4e.org",80))

commond='GET http://data.pr4e.org/intro-short.txt '.encode()

my_sock.send(commond)


while True:
    data=my_sock.recv(500)
    if(len(data)<1):
        break
    print(data.decode(),end='')
    
my_sock.close()

