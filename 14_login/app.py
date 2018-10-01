# Team xD
# Joan Chirinos, Cheryl Qian

from flask import Flask, render_template, request, session, url_for, redirect
import os
app = Flask(__name__) #create instance of class Flask

app.secret_key = os.urandom(32)

@app.route('/')
def login_screen():
    if 'username' in session:
        return render_template('login.html', username=session['username'])
    else:
        return render_template('login.html', username='')

@app.route('/auth')
def authenticate():
    username = request.args['username']
    password = request.args['password']

    session['username'] = username

    straw = open('data/info.txt', 'r')
    text = straw.read()
    straw.close()

    d = {}

    for i in text.split('\n'):
        if i == '':
            break
        x = i.split(',')
        d[x[0]] = x[1]

    if username in d and d[username] == password:
        return redirect(url_for('welcome'))
    else:
        return 'nani'

@app.route('/welcome')
def welcome():
    username = session['username']
    return render_template('welcome.html', name=username)

if __name__ == '__main__':
    app.debug = True
    app.run()
