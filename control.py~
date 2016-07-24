# Flask server, woo!
#

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import json, requests, itertools
from titlecase import titlecase
import datetime 

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

    headers = {'Authorization': 'token %s' % '4ddacff158ceb607f1a6740c675e50af6fc5808a'}
    url = 'https://api.github.com/users/tylerkontra/repos'
    res = []
    r = requests.get(url,headers)
    print(r.text)
    data = json.loads(r.text)
    for dict in r.json():
        repo_name = titlecase(dict.get('name'))
        repo_url = (dict.get('html_url'))
        repo_dsc = (dict.get('description'))
        res.append([repo_name, repo_url, repo_dsc])
        res = sorted(res)

    


    activity_url = 'https://api.github.com/users/tylerkontra/events'
    req = requests.get(activity_url, headers=headers)
    
    acts = json.loads(req.text)
    i = 0
    report=[]
    for event in acts:
	type=(event['type'])
	date=(event['created_at'])
	date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
	date = datetime.datetime.date(date).strftime("%Y-%m-%d")
	repo=(event['repo']['name']).split('/')[1]
	if type == 'PullRequestEvent':
	    title = event['payload']['pull_request']['title']
	    act = [type, date, repo,title]
	    report.append(act)
	else:
	    act = [type, date, repo,'']
	    report.append(act)

        
    return render_template('projects.html',repos=res,report=report)

if __name__ == '__main__':
  app.run()
