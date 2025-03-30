import pybase64
import secrets
import traceback
import asyncio
import os
from dotenv import load_dotenv
from flask import Flask, make_response, request, jsonify
from flask_cors import CORS
from okta_jwt_verifier import BaseJWTVerifier


app = Flask(__name__)
app.config.update({'SECRET_KEY': secrets.token_urlsafe()})
CORS(app)

load_dotenv('.okta.env')

ORG_URL = os.getenv('ORG_URL')

async def verify_token_async(token, issuer):
    print(token)
    """Verify access token."""
    jwt_verifier = BaseJWTVerifier(issuer=issuer, audience='api://default')
    try:
        await jwt_verifier.verify_access_token(token)
        print(token)
        headers, claims, signing_input, signature = jwt_verifier.parse_token(token)
        return claims
    except Exception as e:
        print(f"An error occurred while verifying the token: {e}")
        traceback.print_exc()
        return None

def is_authorized(request):
    """Get verify and get claims from access token."""
    try:
        token = request.headers.get("Authorization").split("Bearer ")[1]
        claims = asyncio.run(verify_token_async(token, f'{ORG_URL}'))
        return claims
    except Exception:
        return None
    
@app.route("/api/whoami")
def whoami():
    claims = is_authorized(request)
    print(claims)
    if not claims:
        return "Unauthorized", 401
    else:
        return make_response(jsonify(claims), 200)

@app.route("/api/hello")
def get_anonymous():
    return "You are anonymous."

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
