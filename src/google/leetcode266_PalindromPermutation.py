
class Solution(object):
    """
    @ Google, Uber

    Given a string, determine if a permutation of the string could form a palindrome.

    For example,
    "code" -> False, "aab" -> True, "carerac" -> True.
    """
    def canPermutePalindrome(self, s): # O(n) time, O(n) space
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        adict = {}
        if n==0 or n==1: return True
        for ch in s:
            if ch in adict:
                adict[ch] += 1
            else:
                adict[ch] = 1
        odds = 0
        for key, value in adict.items():
            if value & 1 != 0:
                odds += 1
        if (n & 1 != 0 and odds == 1) or (n & 1 == 0 and odds == 0):
            return True
        return False