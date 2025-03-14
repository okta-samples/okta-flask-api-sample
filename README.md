# Python Flask API Quickstart Sample Code for Integrating with Okta
 
This repository contains a sample of protecting API endpoints in a custom resource server using a custom authorization server in [Okta](https://www.okta.com/). This sample uses [machine-to-machine sign-in flow](https://developer.okta.com/docs/guides/protect-your-api/python/main/) to protect the API. 

The sample uses the [Okta JWT Verifier SDK](https://github.com/okta/okta-jwt-verifier-python). Read more about getting started with Okta and authentication best practices on the [Okta Developer Portal](https://developer.okta.com).

This code sample demonstrates
* Configuring Okta
* Protecting routes
* Verifying the JWT

## Prerequisites - create an OIDC organization in Okta

Create a free Okta Developer account to create your Okta organization. You can do this through the [Okta CLI](https://cli.okta.com/) or through the [Okta Developer admin](https://developer.okta.com) dashboard.

When using the Okta CLI run the following command:

```shell
okta register
```

Ensure that your default custom authorization server has an access policy. Add an access policy if it's not there. See [Create access polices](https://help.okta.com/okta_help.htm?type=oie&id=ext-create-access-policies).

You will need your Okta domain and Audience.

Update server.js with your Okta settings.

```
ORG_URL = 'https://{yourOktaDomain}/oauth2/default'

async def verify_token_async(token, issuer):
    """Verify access token."""
    jwt_verifier = BaseJWTVerifier(issuer=issuer, audience='api://default')
```

## Run the Example

To run this application, install its dependencies:

```
pip install -r requirements.txt
```

With variables set, start your app:

```
python3 -m flask run --port=5000
```

Use your favorite HTTP Client to call the API. For authenticated calls, follow the steps in [Send a request to your API endpoint using Postman]() of the quick start.

## Helpful resources

* [Learn about Authentication, OAuth 2.0, and OpenID Connect](https://developer.okta.com/docs/concepts/)
* [Get started with Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/)

## Help

Please visit our [Okta Developer Forums](https://devforum.okta.com/).
