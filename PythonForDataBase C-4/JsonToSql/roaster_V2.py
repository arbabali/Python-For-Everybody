

import sqlite3



conn=sqlite3.connect('emaildb2.sqlite')

cur=conn.cursor()

cur.executescript('''
                  
                  DROP TABLE IF EXISTS EMAIL_table ;
                  
                  CREATE TABLE EMAIL_TABLE (email TEXT,count INTEGER,DOMAIN TEXT);
''')

fname='mbox.txt'
fh=open(fname)

for line in fh:
    
    if(line.startswith('From:')):
        
        words=line.split()
        cur.execute('SELECT count from EMAIL_TABLE where email=?',(words[1],))
        current_count=(cur.fetchone())
        
        if current_count is None:
            cur.execute('INSERT INTO EMAIL_TABLE (email,count,domain) VALUES (?,1,?)',(words[1],words[1].split('@')[1]))
       
        else:
            cur.execute('''
                         UPDATE EMAIL_TABLE  SET count=count+1 WHERE email=?
            ''',(words[1],))
           
       # print(words[1].split('@'))
       
    conn.commit()

cur.close()