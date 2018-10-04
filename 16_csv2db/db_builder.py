#Team Dx
#Joan Chirinos, Soojin Choi
#SoftDev1 pd08
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

with open('peeps.csv', newline='\n') as peeps:
    peepDictReader = csv.DictReader(peeps)
    c.execute("CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER PRIMARY KEY);")
    for each in peepDictReader:
        command = "INSERT INTO peeps VALUES('" + each['name'] + "', " + each['age'] + ", " + each['id'] + ");"#build SQL stmt, save as string\
        print(command)
        c.execute(command)    #run SQL statement

with open('courses.csv', newline='\n') as courses:
    courseDictReader = csv.DictReader(courses)
    c.execute("CREATE TABLE courses(name TEXT, mark INTEGER, id INTEGER PRIMARY KEY);")
    for each in courseDictReader:
        command = "INSERT INTO peeps VALUES('" + each['name'] + "', " + each['age'] + ", " + each['id'] + ");"#build SQL stmt, save as string\
        print(command)
        c.execute(command)    #run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
