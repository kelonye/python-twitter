#!/usr/bin/env python
import xml.etree.cElementTree as etree
from cgi import escape
import re
import oauth
from oauth import OAuthConsumer, OAuthRequest


# configurable vars
api_version = 1.1
consumer_key = None
consumer_secret = None


SIGNATURE_METHOD = oauth.OAuthSignatureMethod_HMAC_SHA1()
BASE_API_URI = 'https://api.twitter.com/'+str(api_version)


class MissingKeyError(Exception):
    pass


class InvalidAccessToken(Exception):
    pass


def build(http_url, token, http_method='GET'):

    # build and return oauth request url
    
    match = re.match('(.+):(.+)@(.+)', token)
        
    try:
        token = oauth.OAuthToken(
            match.group(1),
            match.group(2)
        )
    except Exception:
        raise InvalidAccessToken('the provided access token is invalid.')
    
    url = BASE_API_URI + http_url

    if not consumer_key:
        raise MissingKeyError('provide consumer key')
    if not consumer_secret:
        raise MissingKeyError('provide consumer consumer_secret')
    oauth_consumer = oauth.OAuthConsumer(consumer_key, consumer_secret)

    request = OAuthRequest.from_consumer_and_token(
        oauth_consumer,
        http_url=url,
        token=token,
        http_method=http_method,
        parameters={}
    )
    
    request.sign_request(SIGNATURE_METHOD, oauth_consumer, token)

    return request.to_url()
