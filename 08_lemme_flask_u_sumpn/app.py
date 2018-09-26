from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route('/') #assign fxn to route
def hello_world():
    print('the __name__ of this module is...')
    print(__name__) #where will this go?
    return 'No hablo queso!\n<br>Try the subdirectories...<ul><li><a href="/Joan">/Joan</a></li><li><a href="/NotJoan">/NotJoan</a></li></ul>'

@app.route('/Joan')
def display_Joan():
    return 'Hey you found Joan!'

@app.route('/NotJoan')
def display_NotJoan():
    return 'Wait this isn\'t Joan...'

if __name__ == '__main__':
    app.debug = True
    app.run()
