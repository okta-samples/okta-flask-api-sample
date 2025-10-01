# Python Flask API Quickstart Sample Code for Integrating with Okta
 
This repository contains a sample of protecting API endpoints in a custom resource server using a custom authorization server in [Okta](https://www.okta.com/). 

The sample uses the [Okta JWT Verifier SDK](https://github.com/okta/okta-jwt-verifier-python). Read more about getting started with Okta and authentication best practices on the [Okta Developer Portal](https://developer.okta.com).

This code sample demonstrates
* Configuring Okta
* Protecting routes
* Verifying the access token

## Use Case

Your OIDC/OAuth 2.0 enabled app can request resources from a resource server. You will need to bring your own HTTP Client or OIDC app (or use one of ours) and make a resource request to this API. The calling application sends the access token to the resource server using the `Authorization` header. 

```http
GET /api/whoami HTTP/1.1
Authorization: Bearer <access_token_value>
Accept: application/json
```

## Prerequisites

Before you begin, you’ll need an Okta Integrator Free Plan account. To get one, sign up for an [Integrator account](https://developer.okta.com/login). Once you have an account, sign in to your [Integrator account](https://developer.okta.com/login). 

Ensure that your [default custom authorization server](https://developer.okta.com/docs/concepts/auth-servers/#default-custom-authorization-server) has an access policy. Add an access policy if it's not there. See [Create access polices](https://help.okta.com/okta_help.htm?type=oie&id=ext-create-access-policies). Note the Issuer and Audience for the Authorization Server. You need this value for the access token validation.

Configure your client application to authenticate with Okta using OIDC. The client uses the custom authorization server as the Issuer. Note the Client ID of the application. You need this value for access token validation.

## Get the Code

Clone the repo locally by running

```sh
git clone https://github.com/okta-samples/okta-flask-api-sample.git

```

Navigate into the project directory.


## Run the Example

To run this application, install its dependencies:

```sh
pip3 install -r requirements.txt
```

Note - we recommend you use a Python Virtual Environment for testing.

Set the `ISSUER` and `CLIENT_ID` variables in the `.okta.env` file. Use the custom authorization server issuer and your client application's Client ID.

With variables set, start your app:

```sh
python3 -m flask --app server.py run 
```

Use your favorite HTTP Client (or the client app) to call the API endpoints http://127.0.0.1:5000/api/hello and http://127.0.0.1:5000/api/whoami. For authenticated calls, follow the steps in [Send a request to your API endpoint using Postman](https://developer.okta.com/docs/guides/protect-your-api/python/main/#test-with-postman) of the quick start. You can also edit one of our SPA or mobile samples to call this API with the access token.

## Helpful resources

* [Learn about Authentication, OAuth 2.0, and OpenID Connect](https://developer.okta.com/docs/concepts/)
* [Get started with Flask](https://flask.palletsprojects.com/en/stable/quickstart/)

## Help

Please visit our [Okta Developer Forums](https://devforum.okta.com/).
