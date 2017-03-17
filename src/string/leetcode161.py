
class Solution(object):
    """
    @ Snapchat, Uber, Facebook, Twitter

    Given two strings S and T, determine if they are both one edit distance apart.
    """
    def isOneEditDistance_dp(self, s, t):  # O(n^2) time, O(n^2) space
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s) + 1, len(t) + 1
        # table[i][j] indicates the edit distance from s[:i] to t[:j]
        table = [[0] * n for _ in range(m)]

        # initialize the table
        table[0][0] = 0
        for j in range(1, n):
            table[0][j] = j
        for i in range(1, m):
            table[i][0] = i

        # populate the table
        for i in range(1, m):
            for j in range(1, n):
                if s[i - 1] == t[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
        return table[m - 1][n - 1] == 1

    def isOneEditDistance(self, s, t): # O(max(len(s),len(t)) time, O(1) space
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def match(s, t):
            if len(s) != len(t):
                return False
            for i in range(len(s)):
                if s[i] != t[i]:
                    return False
            return True

        if len(s) < len(t):
            s, t = t, s
        m, n = len(s), len(t)
        # s and t are both empty strings
        if m == 0:
            return False
        # s has one character, return True if either t is empty,
        # or t has one character, but it's not same as s.
        if m == 1:
            return n == 0 or s[0] != t[0]
        i = 0
        while i < n:
            if s[i] != t[i]:
                if m == n:
                    return match(s[i + 1:], t[i + 1:])
                else:
                    return match(s[i + 1:], t[i:])
            i += 1
        # for the case, in which s is same as t, except for the last character.
        return i + 1 == m


if __name__ == "__main__":
    s = "a"
    t = "A"
    res = Solution().isOneEditDistance(s, t)
    print res