
import string
import random


class Codec:
    """
    @ Amazon, Google, Uber, Microsoft
    
    Hash Table
    
    TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl 
    and it returns a short URL such as http://tinyurl.com/4e9iAk.

    Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode 
    algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be 
    decoded to the original URL.
    """

    def __init__(self):
        self.base = string.digits + string.lowercase + string.uppercase
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.url2code:
            code = ''.join(random.choice(self.base) for _ in range(6))
            if code not in self.code2url:
                self.url2code[longUrl] = code
                self.code2url[code] = longUrl
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]
