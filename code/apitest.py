import datetime

import json, requests
'''
headers = {'Authorization': 'token %s' % '4ddacff158ceb607f1a6740c675e50af6fc5808a'}


url = 'https://api.github.com/users/tylerkontra/repos'

res = []
r = requests.get(url, headers=headers)
print(r.text)
data = json.loads(r.text)
for iter in r.json():
    repo_name = (iter.get('name'))
    repo_url = (iter.get('html_url'))
    repo_dsc = (iter.get('description').capitalize())
    res.append([repo_name,repo_url,repo_dsc])
    res = sorted(res)

print(res)

activity_url = 'https://api.github.com/users/tylerkontra/events'
req = requests.get(activity_url, headers=headers)


def id_generator(iter,targets):
    for k, v in iter.items():
        if k in targets:
            yield v
        elif isinstance(v,(dict)):
            for id_val in id_generator(v,targets):
                yield id_val


acts = json.loads(req.text)
print(acts)
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
        print(type,date,repo)
        act = [type, date, repo]
        report.append(act)
print(report)


                print(repo)
                i += 1
                print(message)

headers = {'Authorization': 'token %s' \
                                % '4ddacff158ceb607f1a6740c675e50af6fc5808a'}
#REPO TRACKER
url = 'https://api.github.com/users/tylerkontra/repos'
res = []
r = requests.get(url, headers)
print
r.text
data = json.loads(r.text)
for dict in r.json():
    fork_ind = dict.get('fork')
    repo_name = (dict.get('name'))
    repo_url = dict.get('html_url')
    repo_dsc = dict.get('description')
    if fork_ind == False:
        res.append([repo_name, repo_url, repo_dsc])
    res = sorted(res)

print(res)'''
headers = {'Authorization': 'token %s' \
                                % '4ddacff158ceb607f1a6740c675e50af6fc5808a'}
activity_url = 'https://api.github.com/users/tylerkontra/events'
req = requests.get(activity_url, headers=headers)

acts = json.loads(req.text)
report = []
for event in acts:
    typeind = event['type']
    date = event['created_at']
    date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    date = datetime.datetime.date(date).strftime("%Y-%m-%d")
    repo = (event['repo']['name']).split('/')[1]
    if typeind == 'PullRequestEvent':
        title = event['payload']['pull_request']['title']
        act = [typeind, date, repo, title]
        report.append(act)
    else:
        act = [typeind, date, repo, '']
        report.append(act)

print(report)