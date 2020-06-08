import requests, json
import csv

# the URL of the PAP API
#url = 'http://127.0.0.1:5000/pap'
url = 'https://pipcar.herokuapp.com/pap'

# the abstract entities r, v, ay, ctx as well as org
data = {
'org':'caraccess',
'role': 'normal',
'view': 'normal',
'activity': 'a1',
'context': 'off'
}

# prepare and post the request to the PAP using HTTP
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

r = requests.post(url, data=json.dumps(data), headers=headers)

print(r.text)
