#Team Pupps -- Joan Chirinos, Susan Lin
#SoftDev pd08
#K24 -- A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template, request, session, url_for, redirect
import urllib.request, ssl
app = Flask(__name__) #create instance of class Flask

@app.route('/')
def root():
    url = 'https://api.nasa.gov/planetary/apod?api_key=x9CuMbqcX0mo5j5BF8pQGYaTx7R7dGSqSsOUQpmk'
    json_text = urllib.request.urlopen(url)
    print('\n\n\n\n\n\n\n\n\nOpened url\n\n\n\n\n\n\n\n\n')
    json_dict = json.loads(json_text)

    title = json_dict['title']
    content = json_dict['content']
    img_url = json_dict['url']

    return render_template('base.html', title=title, content=content, img_url=img_url)


if __name__ == '__main__':
    app.debug = True
    app.run()
