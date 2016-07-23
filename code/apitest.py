import json, requests
from titlecase import titlecase

url = 'https://api.github.com/users/tylerkontra/repos'

res = []
r = requests.get(url)
print(r.text)
data = json.loads(r.text)
for dict in r.json():
    repo_name = titlecase(dict.get('name'))
    repo_url = (dict.get('html_url'))
    repo_dsc = (dict.get('description').capitalize())
    res.append([repo_name,repo_url,repo_dsc])
    res = sorted(res)

print(res)