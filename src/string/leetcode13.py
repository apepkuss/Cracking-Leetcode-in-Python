

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        result = dict[s[n-1]]
        for x in xrange(n-2, -1, -1):
            if dict[s[x]] >= dict[s[x+1]]:
                result += dict[s[x]]
            else:
                result -= dict[s[x]]
        return result
