from flask import Flask, render_template, request
app = Flask(__name__) #create instance of class Flask

col = [0, 1]
while len(col) < 7:
    col += [col[-1] + col[-2]]

@app.route('/') #assign fxn to route
def main():
    print(app)
    return render_template('mft.html')

@app.route('/auth')
def authenticate():
    return render_template('out.html', name=request.args['username'], req_method=request.method)

if __name__ == '__main__':
    app.debug = True
    app.run()
