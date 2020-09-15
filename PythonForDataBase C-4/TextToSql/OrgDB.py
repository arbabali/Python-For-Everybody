# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 14:55:07 2020

@author: Arbab Ali
"""


import sqlite3
#CONNECTION OR CREATING A FILE 
conn=sqlite3.connect('orgCount.sqlite')
#A CURSOR TO WORK ON WITH SQL OPERATIONS 
cur=conn.cursor()

#TO DELELTE TABLE IF EXIST ALREAD
cur.execute('''
   
            DROP TABLE IF EXISTS Counts
'''
)
#CREATE TABLE WITH FIELDS
cur.execute( '''
        
        CREATE TABLE Counts (org TEXT,count INTEGER)
        '''
        )

#READING A FILE 

fname='mbox.txt'

if (len(fname)<1): fname='default.txt'

fh=open(fname)
for line in fh:
    
    if not line.startswith('From: '):continue
    pieces =line.split()
    email=pieces[1]
    domain=email.split("@")[-1]
    cur.execute('SELECT count FROM Counts WHERE  org = ? ',(domain,))
    row=cur.fetchone()

    if row is None:
        cur.execute('''
                    
            INSERT INTO Counts (org,count) VALUES (?,1)
        ''',(domain,))
    else:
        cur.execute('''
                
           UPDATE Counts SET count=count+1 where org=?
        ''',(domain,))
        
    
conn.commit() #TO SAVE THE CHANGES WE MADE    
sqlqry='SELECT org,count FROM Counts order by count DESC'

# LETS PRINT OUR DATA 

for row in cur.execute(sqlqry):
    print(str(row[0]),row[1])
    
    
cur.close()