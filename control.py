# Flask server, woo!
#

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import json, requests, itertools
from titlecase import titlecase

# Setup Flask app.
app = Flask(__name__)
app.debug = True

@app.route('/')
def root():
  return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)


@app.route('/pages/projects.html')
def projects():

    url = 'https://api.github.com/users/tylerkontra/repos'
    res = []
    r = requests.get(url)
    print(r.text)
    data = json.loads(r.text)
    for dict in r.json():
        repo_name = titlecase(dict.get('name'))
        repo_url = (dict.get('html_url'))
        repo_dsc = (dict.get('description'))
        res.append([repo_name, repo_url, repo_dsc])
        res = sorted(res)

    return render_template('projects.html',repos=res)

if __name__ == '__main__':
  app.run()
