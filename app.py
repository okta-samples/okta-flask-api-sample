import pybase64

from dotenv import load_dotenv
from flask import Flask, make_response, render_template, redirect, request, url_for
from flask_cors import CORS

load_dotenv('.okta.env')

app = Flask(__name__)
CORS(app)

STATE = {}

@app.before_request
def read_authorization_header():
    auth_header = request.headers.get('Authorization')
    if auth_header != None:
        bearer_removed = auth_header.lstrip("Bearer ")
        sections = bearer_removed.split('.')
        # header = sections[0]
        payload = sections[1]
        # signature = sections[2]
        jsonPayload = pybase64.b64decode(payload + '==')
        STATE["authpayload"]=jsonPayload
    else:
        STATE["authpayload"]=None

@app.route("/whoami")
def whoami():
    if STATE["authpayload"] != None:
        response = make_response(STATE["authpayload"])
        return response
    else:
        return make_response("anonymous")

@app.route("/hello")
def get_anonymous():
    return "you are anonymous"

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
