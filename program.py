'''
THE DYNAMIC CODE GROUP
ALL RIGHTS RESERVED 2022
github.com/DynamicCodeGroup
'''

import sqlite3 as sl #Importing the database library
import os, time
import tools.portal as portal

dbConnect = None
db = None

def DBHandler():
    global dbConnect
    global db

    dbConnect = sl.connect('scoring.db') #Connect to DB
    db = dbConnect.cursor() #For running SQL Commands

    #Table does not exist, create one.
    try:
        db.execute("""
        CREATE TABLE Players (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            team TEXT,
            score1 INTEGER,
            score2 INTEGER,
            score3 INTEGER,
            score4 INTEGER,
            score5 INTEGER,
            event1 TEXT,
            event2 TEXT,
            event3 TEXT,
            event4 TEXT,
            event5 TEXT
        );""")
        dbConnect.commit()

    except:
        pass
    
def AppMenu():
    while True:
        os.system('cls')
        print('''
        Scoring Dashboard

        
    <V> View Entries
    <A> Add Entries
    <D> Delete Entries
    <X> Exit Program

-----------------------------------''')

        chooseFrom = ['V', 'A', 'D', 'X']
        choice = input('\n').upper()
        if choice in chooseFrom:
            portal.tp(dbConnect, db, choice)
        else:
            pass

DBHandler()
AppMenu()

'''
NOTES

dbConnect = db
    db = cursor
    db.execute('SELECT * FROM Players')

    data = db.fetchall()
    for row in data:
        print(row)

TEAM && PERSON
(A) 1st = 3,,,, 2nd = 2,,,, 3rd = 1,,,, 4th = 0
(S) 1st = 4,,,, 2nd = 3,,,, 3rd = 2,,,, 4th = 1

'''