
class Solution(object):
    """
    @ Amazon, Bloomberg, Microsoft

    Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

    Examples:

    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.
    Note: You may assume the string contain only lowercase letters.
    """
    def firstUniqChar_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s ) ==0: return -1
        dict = {}
        for i in xrange(len(s)):
            if not dict.has_key(s[i]):
                dict[s[i]] = [i, 1]
            else:
                dict[s[i]][1] += 1
        idx = -1
        for key in dict.keys():
            if dict[key][1] == 1:
                if idx == -1:
                    idx = dict[key][0]
                else:
                    idx = min(idx, dict[key][0])
        return idx

    def firstUniqChar_2(self, s):
        import collections
        x = collections.Counter(s) # return a dict, in which key is character, value is the number of the character in s
        for i, c in enumerate(s):
            if x[c] == 1:
                return i
        return -1