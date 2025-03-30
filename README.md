# Python Flask API Quickstart Sample Code for Integrating with Okta
 
This repository contains a sample of protecting API endpoints in a custom resource server using a custom authorization server in [Okta](https://www.okta.com/). This sample uses [machine-to-machine sign-in flow](https://developer.okta.com/docs/guides/protect-your-api/python/main/) to protect the API. 

The sample uses the [Okta JWT Verifier SDK](https://github.com/okta/okta-jwt-verifier-python). Read more about getting started with Okta and authentication best practices on the [Okta Developer Portal](https://developer.okta.com).

This code sample demonstrates
* Configuring Okta
* Protecting routes
* Verifying the JWT

## Prerequisites - create an OIDC organization in Okta

Create a free Okta Developer account to create your Okta organization. You can do this through the [Okta CLI](https://cli.okta.com/) or through the [Okta Developer admin](https://developer.okta.com) dashboard.


* An Okta Developer Account (create one using `okta register`, or configure an existing one with `okta login`)

Ensure that your [default custom authorization server](https://developer.okta.com/docs/concepts/auth-servers/#default-custom-authorization-server) has an access policy. Add an access policy if it's not there. See [Create access polices](https://help.okta.com/okta_help.htm?type=oie&id=ext-create-access-policies).

## Get the Code

Grab and configure this project using `okta start flask-api`.

Follow the instructions printed to the console. 

## Run the Example

To run this application, install its dependencies:

```
pip3 install -r requirements.txt
```

With variables set, start your app:

```
python3 -m flask --app server.py run 
```

Use your favorite HTTP Client to call the API endpoints http://127.0.0.1:5000/api/hello and http://127.0.0.1:5000/api/whoami. For authenticated calls, follow the steps in [Send a request to your API endpoint using Postman](https://developer.okta.com/docs/guides/protect-your-api/python/main/#test-with-postman) of the quick start.

## Helpful resources

* [Learn about Authentication, OAuth 2.0, and OpenID Connect](https://developer.okta.com/docs/concepts/)
* [Get started with Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/)

## Help

Please visit our [Okta Developer Forums](https://devforum.okta.com/).
