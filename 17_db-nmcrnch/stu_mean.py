#Team Watch_Out_For_Snakes
#Joan Chirinos, Mohtasim Howlader


import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

def add_course_row(code, mark id):
    c.execute('INSERT INTO courses VALUES({}, {}, {})'.format(course, mark, id))

def go():
    c.execute('CREATE TABLE peeps_avg(id INTEGER PRIMARY KEY, avg INTEGER)')

    l = c.execute('SELECT peeps.id, mark FROM peeps, courses WHERE peeps.id = courses.id')
    d = {}

    for i in l:
        if i[0] in d:
            d[i[0]] += [i[1]]
        else:
            d[i[0]] = [i[1]]

    for i in d:
        avg = sum(d[i]) / len(d[i])
        c.execute('INSERT INTO peeps_avg VALUES({}, {})'.format(i, avg))

    db.commit()

    x = c.execute('SELECT peeps.name, peeps.id, avg FROM peeps_avg, peeps WHERE peeps.id = peeps_avg.id')
    for i in x:
        print('name: {}\n\tid: {}\n\tavg: {}\n'.format(i[0], i[1], i[2]))

    db.close()

go()
