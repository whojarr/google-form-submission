import os
import json
from flask import Flask, request
import requests


app = Flask(__name__)

SERVERLESS_STAGE = os.environ['SERVERLESS_STAGE'];
TEAMS_URL = os.environ['TEAMS_URL'];
APIKEY = os.environ['APIKEY'];


def send_teams_message(title, summary, text, facts=[]):

    ''' Create the mapping to convert to json containing the teams message '''
    tdata = {}
    tdata['@context'] = "http://schema.org/extensions"
    tdata['@type'] = "MessageCard"
    tdata['themeColor'] = "00FF00"
    tdata['title'] = title
    tdata['sections'] = [{"facts": facts}]
    tdata['summary'] = summary
    tdata['text'] = text
    print(json.dumps(tdata, indent=4))
    ''' Send a teams formated dict to a teams channel '''
    response = requests.post(
        TEAMS_URL, data=json.dumps(tdata),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to Teams returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )


@app.route("/", methods=["GET", "POST"])
def event():

    data = request.json
    qs = data['questions']
    facts = []
    for key, value in qs.items():
        facts.append({"name": key[:128], "value": str(value)[:128]})

    send_teams_message("google form submission", "google form submission", "google form submission", facts=facts)

    resp = app.response_class(
        response=json.dumps('{"Result": "got it"}'),
        status=200,
        mimetype='application/json'
    )
    return resp

if __name__ == "__main__":

    facts = []
    with open('samples/ltmd.json', 'r') as questions:
        data = json.load(questions)
        qs = data['questions']
    for key, value in qs.items():
        facts.append({"name": key[:128], "value": str(value)[:128]})
    #print(facts)
    send_teams_message("google form submission test", "google form submission test", "google form submission test", facts=facts)