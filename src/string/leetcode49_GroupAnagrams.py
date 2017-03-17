
class Solution(object):
    """
    @ Amazon, Bloomberg, Uber, Facebook, Yelp

    Given an array of strings, group anagrams together.
    For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
    Return:
        [
        ["ate", "eat","tea"],
        ["nat","tan"],
        ["bat"]
        ]
    Note: All inputs will be in lower-case.
    """
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        if strs is None: 
            return res
        
        n = len(strs)
        if n <= 1: 
            res.append(strs)
            return res
        adict = {}
        for i in xrange(n):
            # notice how to sort a unicode string
            key = ''.join(sorted(strs[i]))
            if key in adict:
                adict[key].append(strs[i])
            else:
                adict[key] = [strs[i]]
                
        for _, value in adict.items():
            res.append(value)
        return res