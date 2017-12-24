import sqlite3
import datetime
import os
import wget

#os.remove('powerball.db')

def insertToDB(pbFile):
    conn=sqlite3.connect('powerball.db')

    c=conn.cursor()
    #create a table
    c.execute('''CREATE TABLE powerball
                (id integer primary key, drawnDate text UNIQUE, wb1 integer, wb2 integer,wb3 integer,wb4 integer,wb5 integer,pb integer)
                ''')
    #f=open('powerBall.txt','r')
    f=open(pbFile,'r')
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

#Gets the latest powerball file
def getFile():
    try:
        os.remove('winnums-text.txt')
    except:
        pass
    url=" http://www.powerball.com/powerball/winnums-text.txt"
    powerBallFile=wget.download(url)
    return powerBallFile

def updateDB():
    return

