#!/usr/bin/env python
import unittest
import urllib2
import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import lib as twitter

twitter.consumer_key = os.environ.get('TWITTER_LIB_KEY')
twitter.consumer_secret = os.environ.get('TWITTER_LIB_SECRET')
twitter.testing = True


class Test(unittest.TestCase):

    def test_get(self):

        token = ''
        url = twitter.build('/account/verify_credentials.json', token)
        response = urllib2.urlopen(url)
        print json.dumps(json.loads(response.read()), indent=2)


if __name__ == '__main__':
    unittest.main()