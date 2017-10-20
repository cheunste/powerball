import sqlite3
import datetime
import os

os.remove('powerball.db')
conn=sqlite3.connect('powerball.db')

c=conn.cursor()
#create a table
c.execute('''CREATE TABLE powerball
            (id integer primary key, drawnDate text, wb1 integer, wb2 integer,wb3 integer,wb4 integer,wb5 integer,pb integer)
            ''')
f=open('powerBall.txt','r')
#This gets rid of the header
f.readline()

for line in f:
    temp= line.split()
    #temp[0]=str(datetime.datetime.strptime(temp[0],"%m/%d/%Y").strftime("%Y-%m-%d"))
    temp[0]=str(datetime.datetime.strptime(temp[0],"%m/%d/%Y").date().isoformat())
    c.execute("INSERT INTO powerball (drawnDate,wb1,wb2,wb3,wb4,wb5,pb)VALUES (?,?,?,?,?,?,?)",(temp[0] ,temp[1],temp[2],temp[3],temp[4],temp[5] ,temp[6]))
    print temp

conn.commit()
conn.close()

