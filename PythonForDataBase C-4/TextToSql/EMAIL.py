
import sqlite3
#CONNECTION OR CREATING A FILE 
conn=sqlite3.connect('emaildb.sqlite')
#A CURSOR TO WORK ON WITH SQL OPERATIONS 
cur=conn.cursor()

#TO DELELTE TABLE IF EXIST ALREAD
cur.execute('''
   
            DROP TABLE IF EXISTS EMAIL_COUNTS
'''
)
#CREATE TABLE WITH FIELDS
cur.execute( '''
        
        CREATE TABLE EMAIL_COUNTS(email TEXT,count INTEGER)
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
    
    cur.execute('SELECT count FROM EMAIL_COUNTS WHERE  email = ? ',(email,))
    row=cur.fetchone()

    if row is None:
        cur.execute('''
                    
            INSERT INTO EMAIL_COUNTS (email,count) VALUES (?,1)
        ''',(email,))
    else:
        cur.execute('''
                
           UPDATE EMAIL_COUNTS SET count=count+1 where email=?
        ''',(email,))
        
    conn.commit() #TO SAVE THE CHANGES WE MADE
    
    
    
sqlqry='SELECT email,count FROM EMAIL_COUNTS order by count DESC'

# LETS PRINT OUR DATA 

for row in cur.execute(sqlqry):
    print(str(row[0]),row[1])
    
    
cur.close()