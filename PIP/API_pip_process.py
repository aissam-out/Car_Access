from flask import Flask, jsonify, request
from utils import *
import csv

app = Flask(__name__)

# PIP API
@app.route('/pip', methods=['POST'])
def index():
    # get concrete entities
    json_content = request.get_json()
    org = json_content['org']
    sub = json_content['subject']
    obj = json_content['object']
    act = json_content['action']
    ctx = json_content['ctx']

    # match concrete and abstract entities
    role = empower(org, sub)[2]
    view = use(org, obj)[2]
    ay = consider(org, act)[2]
    context = check_context(ctx[0], ctx[1])[2]

    fields = [org, role, view, ay, context]
    
    # save fields in request.csv
    with open(r'request.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    return str(fields)

# PAP API
@app.route('/pap', methods=['POST'])
def pap_func():
    # get abstract entities
    json_content = request.get_json()
    org = json_content['org']
    role = json_content['role']
    view = json_content['view']
    activity = json_content['activity']
    context = json_content['context']

    # get decision from PAP
    response = check_decision(org, role, view, activity, context)

    # save reponse in reponse.csv
    with open(r'response.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(response)
    
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
