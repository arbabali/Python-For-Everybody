# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 22:01:16 2020

@author: Arbab Ali
"""

import json 
import sqlite3



conn=sqlite3.connect('roaster.sqlite')

cur=conn.cursor()
#CREATE TABLE 
cur.executescript('''
    
    DROP TABLE IF EXISTS COURSE;
    DROP TABLE IF EXISTS MEMBER ;
    DROP TABLE IF EXISTS USER ;    
    DROP TABLE IF EXISTS USERS;              
    
    
    CREATE TABLE COURSE (title TEXT UNIQUE , id INTEGER PRIMARY  KEY AUTOINCREMENT  UNIQUE );
    CREATE TABLE USER (name text UNIQUE, id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE);
    CREATE TABLE MEMBER ( user_id INTEGER,course_id INTEGER,role INTEGER, PRIMARY KEY (user_id,course_id));
    
''')

#fname=input("ENTER JSON FILE")
#if(len(fname)<1):
fname='roster_data.json'
    

str_data=open(fname).read()
#print(str_data)
json_data=json.loads(str_data)

for entry in json_data:
    #print (entry)
    name=entry[0]
    title=entry[1]
    role=entry[2]
    #print ((name,title))
    
    cur.execute('''insert or ignore into user (name) values (?)''',(name,))
    cur.execute('''select id from user where name =? ''',(name,))
    user_id=(cur.fetchone()[0])
    
    cur.execute('''INSERT OR IGNORE INTO COURSE(title) values (?)''',(title,))
    cur.execute('''SELECT id from course where title=?''',(title,))
    course_id=(cur.fetchone()[0])
    
    cur.execute('''INSERT OR REPLACE into member (user_id,course_id,role) values(?,?,?)''',(user_id,course_id,role))
    
    conn.commit()
    
    
    
    
#print(json.dumps(json_data,indent=4))