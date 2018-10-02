#Team xD -- Joan Chirinos, Cheryl Qian
#SoftDev pd8 
#K14 -- Do I Know You?
#2018-10-02

from flask import Flask, render_template, request, session, url_for, redirect
import os
app = Flask(__name__) #create instance of class Flask

app.secret_key = os.urandom(32)

@app.route('/')
def login_screen():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')

@app.route('/error')
def error(type):
    session.pop('username')
    newError = type
    return render_template('error.html',
                           error = newError)
    

@app.route('/auth', methods=["POST"])
def authenticate():
    username = request.form['username']
    password = request.form['password']

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
    elif username not in d:
        return error('Username does not exist')
    else:
        return error('Wrong password')


@app.route('/welcome')
def welcome():
    username = session['username']
    return render_template('welcome.html', name=username)

if __name__ == '__main__':
    app.debug = True
    app.run()
