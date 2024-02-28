import pybase64
import secrets

from dotenv import load_dotenv
from flask import Flask, make_response, request, session
from flask_cors import CORS

load_dotenv('.okta.env')

app = Flask(__name__)
app.config.update({'SECRET_KEY': secrets.token_urlsafe()})
CORS(app)

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
        session["authpayload"]=jsonPayload
    else:
        session["authpayload"]=None

@app.route("/whoami")
def whoami():
    if session["authpayload"] != None:
        return make_response(session["authpayload"])
    else:
        return make_response("anonymous", 401)

@app.route("/hello")
def get_anonymous():
    return "you are anonymous"

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
