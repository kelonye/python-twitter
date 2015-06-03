
## Install

    $ pip install ptwitter


## Example

Use this libary to make authenticated calls to Twitter's REST API. The library requires you to first obtain a user's access token externally using something like:

- [HelloJS](http://adodson.com/hello.js/)
- [Android](https://github.com/TakahikoKawasaki/TwitterOAuthView)
- [iOS](https://github.com/bengottlieb/Twitter-OAuth-iPhone)

You can then use the obtained token to build the `url` to use to access the desired resource:


```python

import urllib2
import ptwitter as twitter

twitter.consumer_key = 'consumer_key'
twitter.consumer_secret = 'consumer_secret'

token = ''
resource = '/account/verify_credentials.json'
url = twitter.build(resource, token)
response = urllib2.urlopen(url)
print response.read()

```

## Test

    $ make test

## License

MIT
