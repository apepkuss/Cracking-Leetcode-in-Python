import unittest

class Solution(object):
    """
    @ Pocket Gems, Microsoft, Apple, Facebook

    Two Points, String

    Implement strStr(). Returns the index of the first occurrence of needle
    in haystack, or -1 if needle is not part of haystack.
    """

    #
    # KMP (Knuth Morris Pratt) pattern searching: O(n) time, n is the length of text
    #
    # KMP matching algorithm uses degenerating property (pattern having same sub-patterns appearing more than
    # once in the pattern) of the pattern and improves the worst case complexity to O(n).
    #
    # The basic idea behind KMP's algorithm is: whenever we detect a mismatch (after some matches), we already
    # know some of the characters in the text of next window. We take advantage of this information to avoid
    # matching the characters that we know will anyway match.
    #
    # The most important step for KMP's is how to know how many characters to be skipped. To know this, we have
    # to pre-process pattern and prepares an integer array lps[] to store this information.
    #
    #
    # *** Preprocessing Overview:
    #
    # 1. lps[] of size m (same as the length of pattern) is used to skip characters while matching
    # 2. name lps indicates longest proper prefix which also suffix. A proper prefix is prefix with whole string
    #    not allowed. For example, prefixes of 'ABC' are '', 'A', 'AB', and 'ABC'. Proper prefixes are '', 'A'
    #    and 'AB'. Suffixes of the string are '', 'C', 'BC', 'ABC'.
    # 3. For each sub-pattern pattern[0..i] where i = 0 to m-1, lps[i] stores length of the maximum matching
    #    proper prefix which is also a suffix of the sub-pattern pattern[0..i].
    #
    #
    # *** How to use lps[] to decide next positions (or to know number of characters to be skipped)?
    #
    # 1. We start comparison of pattern[j] with j=0 with characters of current window of text.
    # 2. We keep matching characters text[i] and pattern[j] and keep incrementing i and j while text[i] and pattern[j]
    #    keep matching.
    # 3. When we see a mismatching,
    #       3.1. We know that characters pattern[0..j-1] match with text[i-j+1..i-1] (Note that j starts with 0
    #            and increment it only when there is a match).
    #       3.2. We also know (from above definition) that lps[j-1] is count of characters of pattern[0..j-1] that
    #            are both proper prefix and suffix.
    #       3.3. From above two points, we can conclude that we do not need to match these lps[j-1] characters with
    #            text[i-j+1...i-1] because we know that these characters will anyway match.
    #

    def strStr_KMP(self, haystack, needle):  # O(m+n) time, O(n) space
        """
        Get the index of first occurrence of needle in haystack.
        :param haystack: a text of strings
        :param needle: a string
        :return: the index of first occurrence of needle in haystack.
        """
        m, n = len(haystack), len(needle)
        if n == 0: return 0
        if m < n: return -1

        # For each sub-pattern pattern[0..i], lps[i] indicates the length of
        # the maximum proper prefix of it, which is also suffix of it.
        lps = self.compute_lps(needle)

        # traverse haystack in O(m) time
        i = j = 0
        while i < m and j < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = lps[j-1]
                else:
                    i += 1
        if j == n:
            return i - n
        else:
            return -1

    def compute_lps(self, pattern):
        """
        Compute longest prefix-suffix array
        """
        n = len(pattern)

        # For each sub-pattern pattern[0..i], lps[i] indicates the length of
        # the maximum proper prefix of it, which is also suffix of it.
        lps = [0 for _ in xrange(n)]

        # length of current proper prefix
        l = 0

        # the loop computes lps[i] for i = 1 to n-1
        i = 1
        while i < n:
            if pattern[i] == pattern[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l == 0:
                    lps[i] = 0
                    i += 1
                else:
                    l = lps[l-1]
        return lps


class TestRun(unittest.TestCase):

    def test_prefixArray(self):
        pattern = "acacabacacabacacac"
        T = Solution.compute_lps(pattern)
        expected_result = [0,0,1,2,3,0,1,2,3,4,5,6,7,8,9,10,11,4]
        unittest.TestCase.assertEqual(self, first=expected_result, second=T)

    def test_noMatch(self):
        text = "babba"
        pattern = "bbb"
        actual_result = Solution().strStr_KMP(text, pattern)
        expected_result = -1
        unittest.TestCase.assertEqual(self, first=expected_result, second=actual_result)


if __name__ == "__main__":
    unittest.main()
