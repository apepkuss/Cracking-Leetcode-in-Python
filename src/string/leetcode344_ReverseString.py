

class Solution(object):
    """
    Write a function that takes a string as input and returns the string reversed.

    Example:
    Given s = "hello", return "olleh".
    """
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2 or s is None:
            return s
        res = list(s)
        i, j = 0, len(res)-1
        while i < j:
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
        return ''.join(res)