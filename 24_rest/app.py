#Team Pupps -- Joan Chirinos, Susan Lin
#SoftDev pd08
#K24 -- A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template, request, session, url_for, redirect
import urllib.request, json
app = Flask(__name__) #create instance of class Flask

@app.route('/')
def root():
    url = 'https://api.nasa.gov/planetary/apod?api_key=x9CuMbqcX0mo5j5BF8pQGYaTx7R7dGSqSsOUQpmk'
    json_text = urllib.request.urlopen(url)
    json_dict = json.loads(json_text.read())

    # print('DICT:\n{}'.format(json_dict))

    title = json_dict.get('title', 'TITLE')
    content = json_dict.get('explanation', 'NO EXPLANATION')
    media_type = json_dict.get('media_type', 'NO TYPE')
    media_url = json_dict.get('url', 'NO URL')
    media = ''

    if (media_type == 'video'):
        media = '<iframe src={}></iframe>'.format(media_url)
    elif (media_type == 'image'):
        media = '<img src={} style="max-height: 60vh; max-width: 80vw;">'.format(media_url)
    else:
        media = '<p>NO MEDIA</p>'

    return render_template('base.html', title=title, content=content, media=media)


if __name__ == '__main__':
    app.debug = True
    app.run()
