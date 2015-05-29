#!/usr/bin/env python
import unittest
from urllib2 import urlopen

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import lib as twitter

twitter.consumer_key = os.environ.get('TWITTER_LIB_KEY')
twitter.consumer_secret = os.environ.get('TWITTER_LIB_SECRET')
twitter.testing = True


class Test(unittest.TestCase):

    def test_get(self):

        token = ''
        url = '/account/verify_credentials.json'
        print 'open in browser ' + twitter.build(url, token)


if __name__ == '__main__':
    unittest.main()