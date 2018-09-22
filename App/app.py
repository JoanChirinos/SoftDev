from flask import Flask, render_template
app = Flask(__name__) #create instance of class Flask

col = [0, 1]
while len(col) < 7:
    col += [col[-1] + col[-2]]

@app.route('/my_foist_template') #assign fxn to route
def main():
    return render_template('mft.html', collection=col, foo='you\'re mom')

if __name__ == '__main__':
    app.debug = True
    app.run()
