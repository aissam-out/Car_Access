import requests, json
import csv

# the URL of the PIP API
url = 'http://127.0.0.1:5000/pip'
#url = 'https://pipcar.herokuapp.com/pip'

# the concrete entities s, o, a, c, as well as org and id
data = {
'id':'29',
'org': 'caraccess',
'subject': 'EH4127',
'object': 'AS 9684',
'action': 2,
'ctx': ['2020-08-03', '2020-11-29']
}

# prepare and post the request to the PIP using http
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

r = requests.post(url, data=json.dumps(data), headers=headers)

print(r.text)
