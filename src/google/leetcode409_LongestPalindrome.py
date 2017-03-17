

class Solution(object):
    """
    @ Google
    Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

    This is case sensitive, for example "Aa" is not considered a palindrome here.

    Note:
    Assume the length of given string will not exceed 1,010.

    Example:

    Input:
    "abccccdd"

    Output:
    7

    Explanation:
    One longest palindrome that can be built is "dccaccd", whose length is 7.
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2: return len(s)
        adict = {}
        for c in s:
            if c not in adict:
                adict[c] = 1
            else:
                adict[c] += 1
        odd = False
        length = 0
        for _, value in adict.items():
            if value & 1 == 0:
                length += value
            else:
                length += (value/2) * 2
                if not odd:
                    length += 1
                    odd = True
        return length