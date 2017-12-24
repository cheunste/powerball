import sqlite3
import datetime
import os
import wget

def checkDateInDB(drawnDate):
    conn=sqlite3.connect('powerball.db')
    c=conn.cursor()
    result=c.execute("SELECT drawnDate from powerball where drawnDate ==",drawnDate)
    conn.close()
    print "result: "+result

def insertToDB(pbFile,flag):
    conn=sqlite3.connect('powerball.db')
    tableName="statsTable"
    c=conn.cursor()
    #create a table
    if flag == "CREATE":
        c.execute('''CREATE TABLE '''+statsTable+'''
                    (id integer primary key, drawnDate text UNIQUE, wb1 integer, wb2 integer,wb3 integer,wb4 integer,wb5 integer,pb integer)
                    ''')
    #f=open('powerBall.txt','r')
    f=open(pbFile,'r')
    #This gets rid of the header
    f.readline()

    c.execute('''
        SELECT * from powerball
    ''')

    result = c.execute("SELECT * from powerball")
    print result
    conn.commit()
    conn.close()

def readFromDB():
    conn=sqlite3.connect('powerball.db')
    tableName="statsTable"
    c=conn.cursor()
    #create a table
    results = c.execute("SELECT * from powerball")
    tempArr=[]
    for result in results:
        print result
        tableId,drawnDate,wb1,wb2,wb3,wb4,wb5,rb = result
        wbArr=[wb1,wb2,wb3,wb4,wb5]
        wbArr.sort()
        tempArr.append((drawnDate,wbArr))

    print tempArr
    for item in tempArr:
        wbArr=item[1]
        drawnDate=item[0]
        c.execute("INSERT INTO stats (drawnDate, diff1, diff2, diff3, diff4) VALUES (?,?,?,?,?)", (drawnDate,wbArr[1]-wbArr[0],wbArr[2]-wbArr[1],wbArr[3]-wbArr[2],wbArr[4]-wbArr[3]))
    conn.commit()
    conn.close()

if __name__=='__main__':
    readFromDB()
