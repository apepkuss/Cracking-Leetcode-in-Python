
import string
import random


class TinyUrl(object):
    """
    @ Amazon, Google, Uber, Facebook
    
    Design
    
    How would you design a URL shortening service that is similar to TinyURL?

    Background:
    TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl 
    and it returns a short URL such as http://tinyurl.com/4e9iAk.
    
    Requirements:
    For instance, "http://tinyurl.com/4e9iAk" is the tiny url for the page "https://leetcode.com/problems/design-tinyurl". 
    The identifier (the highlighted part) can be any string with 6 alphanumeric characters containing 0-9, a-z, A-Z.
    Each shortened URL must be unique; that is, no two different URLs can be shortened to the same URL.
    
    
    Note about Questions:
    Below are just a small subset of questions to get you started. In real world, there could be many follow ups and 
    questions possible and the discussion is open-ended (No one true or correct way to solve a problem). If you have 
    more ideas or questions, please ask in Discuss and we may compile it here!
    
    Questions:
    How many unique identifiers possible? Will you run out of unique URLs?
    A: 62**6 unique identifiers
    
    Should the identifier be increment or not? Which is easier to design? Pros and cons?
    A: It's not a good way, because if I am asked to encode a same long url many times, it will get several different
       identifiers. That wastes time and memory.
    
    What is the bottleneck of the system? Is it read-heavy or write-heavy?
    A: write-heavy
    
    Estimate the maximum number of URLs a single machine can store.
    A: 62**6 different urls
    
    Estimate the maximum number of queries per second (QPS) for decoding a shortened URL in a single machine.
    A: Decoding a short url needs O(1) time only, if use hash table as storage.
    
    How would you scale the service? For example, a viral link which is shared in social media could result in a peak 
    QPS at a moment's notice.
    How could you handle redundancy? i,e, if a server is down, how could you ensure the service is still operational?
    
    Keep URLs forever or prune, pros/cons? How we do pruning? (Contributed by @alex_svetkin)
    A: If use database as storage, we can keep urls forever, as long as we have enough storage space. If we ran out of
       storage, we can prune the least recently used urls according to their last updated time stamp.
       
    What API would you provide to a third-party developer? (Contributed by @alex_svetkin)
    A: APIs for like creating shorten urls, getting stats like total hits, referrals, last accessed time, etc.
    
    If you can enable caching, what would you cache and what's the expiry time? (Contributed by @Humandroid)
    """

    def __init__(self):
        self.url2code = {}
        self.code2url = {}
        self.base = string.digits + string.lowercase + string.uppercase

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            code = ''.join(random.choice(self.base) for _ in range(6))
            if code not in self.code2url:
                self.url2code[longUrl] = code
                self.code2url[code] = longUrl

        return self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl]