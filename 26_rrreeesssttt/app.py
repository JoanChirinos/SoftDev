#Team Pupps -- Joan Chirinos, Susan Lin
#SoftDev pd08
#K24 -- A RESTful Journey Skyward
#2018-11-13

import urllib.request, json
from datetime import datetime
from random import randrange, choice

from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__) #create instance of class Flask

@app.route('/')
def root():
    return render_template('root.html')

@app.route('/ISS_API')
def iss():
    URL = 'http://api.open-notify.org/iss-now.json'

    response = urllib.request.urlopen(URL).read()
    json_dict = json.loads(response)

    arg_list = {}

    pos = json_dict['iss_position']
    arg_list['longitude'] = pos['longitude']
    arg_list['latitude'] = pos['latitude']

    timestamp = json_dict['timestamp']
    arg_list['time'] = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S UTC')

    return render_template('iss.html', **arg_list)

@app.route('/Skate_Ipsum_API')
def skate():
    paragraph_num = 1
    start_with_ipsum = 1
    URL = 'http://skateipsum.com/get/{}/{}/JSON'

    response = urllib.request.urlopen(URL.format(paragraph_num, start_with_ipsum)).read()
    print('RESPONSE:\n{}'.format(response))
    json_dict = json.loads(response)
    print('\n\nJSON RESPONSE:\n{}'.format(json_dict))

    ipsum = json_dict[0]

    return render_template('skate.html', content=ipsum)

@app.route('/Numbers_API')
def numbers():
    URL = 'http://numbersapi.com/random/{}?json'
    type_list = ['trivia', 'math', 'year']

    valid_number = False
    while (not valid_number):
        response = urllib.request.urlopen(URL.format(choice(type_list))).read()
        print('RESPONSE:\n{}'.format(response))
        json_dict = json.loads(response)
        valid_number = json_dict['found']

    kwargs = {}
    kwargs['number'] = json_dict['number']
    kwargs['fact'] = json_dict['text']
    kwargs['type'] = json_dict['type'].capitalize()

    return render_template('numbers.html', **kwargs)

if __name__ == '__main__':
    app.debug = True
    app.run()
