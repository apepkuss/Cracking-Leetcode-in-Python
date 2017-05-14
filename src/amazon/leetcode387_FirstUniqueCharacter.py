
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

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        adict = {}
        for c in s:
            if c not in adict:
                adict[c] = 1
            else:
                adict[c] += 1

        # use built-in enumerate function
        for i, c in enumerate(s):
            if adict[c] == 1:
                return i

        return -1
