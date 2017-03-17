

class Solution(object):
    def strStr_bruteforce(self, haystack, needle):  # O(m*n) time, O(1) space
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(haystack), len(needle)
        if n == 0: return 0
        if m < n: return -1

        # the range is the most critical part for the performance
        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1

