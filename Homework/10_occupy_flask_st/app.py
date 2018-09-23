# Team StickyToes
# Joan Chirinos, Johnny Wong
# K10 -- Jinja Tuning
# 2018-09-21

from flask import Flask, render_template
from random import random
app = Flask(__name__)

@app.route('/')
def redir():
    return """<html><head></head><body><script>window.onload = function() {
    window.location.href = "/occupations";
}</script></body></html>"""

@app.route('/occupations')
def go():
    d = toDict(read('data/occupations.csv'))
    r = getRandom(d)
    return render_template('template.html', random_occ = r, title = "Occupations", occs = d)


########## Utils ##########
def read(filename):
    straw = open(filename, 'r')
    text = straw.read()
    straw.close
    return text


def toDict(text):
    d = {}
    lines = text.split('\n')[1:]
    while (len(lines) > 0 and lines[-1] == ''):
        lines = lines[:-1]
    for line in lines:
        temp = line.rsplit(',', 2)
        d[temp[0].strip('"')] = [float(temp[1]), temp[2]]
    return d

def getRandom(d):
    total = d['Total'][0]
    goal = random() * total
    for key in d.keys():
        goal -= d[key][0]
        if (goal < 0):
            return key
    return 'Something went horribly wrong Dx'

def getOcc():
    return getRandom(toDict(read('data/occupations.csv')))

########## End utils ##########

if __name__ == '__main__':
    app.debug = True
    app.run()
