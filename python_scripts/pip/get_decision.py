import requests, json
import csv

#url = 'http://127.0.0.1:5000/pap'
url = 'https://pipcar.herokuapp.com/pap'

data = {
'org':'caraccess',
'role': 'normal',
'view': 'normal',
'activity': 'a1',
'context': 'off'
}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

r = requests.post(url, data=json.dumps(data), headers=headers)

print(r.text)
