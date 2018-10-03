#Team xD -- Joan Chirinos, Cheryl Qian
#SoftDev pd8 
#K15 -- Oh yes, perhaps I do…
#2018-10-02

from flask import Flask, render_template, request, session, url_for, redirect, flash
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
    flash('Successfully logged out!')
    return redirect(url_for('login_screen'))

# @app.route('/error')
# def error(type):
#     session.pop('username')
#     newError = type
#     return render_template('error.html',
#                            error = newError)
    

@app.route('/auth', methods=["POST"])
def authenticate():
    username = request.form['username']
    password = request.form['password']

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
        session['username'] = username
        return redirect(url_for('welcome'))
    elif username not in d:
        print("Username does not exist!")
        flash("Username does not exist!")
        return redirect(url_for('login_screen'))
    else:
        print("Password incorrect!")
        flash("Password incorrect!")
        return redirect(url_for('login_screen'))
        #return error('Wrong password')


@app.route('/welcome')
def welcome():
    username = session['username']
    return render_template('welcome.html', name=username)

if __name__ == '__main__':
    app.debug = True
    app.run()
