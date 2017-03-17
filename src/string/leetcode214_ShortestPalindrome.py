
class Solution(object):
    """
    @ Pocket Gems, Google

    Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

    For example:

    Given "aacecaaa", return "aaacecaaa".

    Given "abcd", return "dcbabcd".
    """
    def shortestPalindrome_KMPPrefixTable(self, s):
        """
        :type s: str
        :rtype: str
        """
        ns = s + '#' + s[::-1]
        n = len(ns)
        length = 0

        ### Subroutine of building longest prefix-suffix table of KMP Algorithm ###
        # length of longest prefix-suffix substring
        lps = [0] * n
        i = 1
        while i < n:
            if ns[i] == ns[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length == 0:
                    lps[i] = 0
                    i += 1
                else:
                    length = lps[ length -1]
        ############################################################################
        return s[lps[n-1]:][::-1] + s


if __name__ == "__main__":
    s = "aacecaaa"
    res = Solution().shortestPalindrome_KMPPrefixTable(s)
    print res
