# Team StickyToes
# Joan Chirinos, Johnny Wong
# K12 -- 
# 2018-09-25

from flask import Flask, render_template

#importing utility tools for occupations
from util import occupations as o

app = Flask(__name__) #instantiate flask obj

# redirects root dir to /occupations
@app.route('/')
def redir():
    return """<html><head></head><body><script>window.onload = function() {
    window.location.href = "/occupations";
}</script></body></html>"""

@app.route('/occupations')
def go():
    d = o.toDict(o.read('data/occupations.csv')) # occupation dictionary
    r = o.getRandom(d) # random occupation
    return render_template('template.html', random_occ = r, title = "Occupations", occs = d)

if __name__ == '__main__':
    app.debug = True
    app.run()
