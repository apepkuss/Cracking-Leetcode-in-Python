

class Solution(object):

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def dfs(s, offset, valuelist):
            if len(s) == 0:
                res.append(valuelist)
                return
            # try each possible sub-string by backtracking algorithm
            for l in range(1, len(s) + 1):
                if table[0+offset][l-1+offset]:
                    dfs(s[l:], offset+l, valuelist + [s[:l]])

        def buildTable(s):
            """
            Build a memorization table for later look-up
            """
            n = len(s)
            table = [[False] * n for _ in xrange(n)]
            for length in xrange(1, n + 1):
                for i in xrange(n - length + 1):
                    j = (i + length - 1) % n
                    if i == j:
                        table[i][j] = True
                    elif i == j - 1:
                        table[i][j] = s[i] == s[j]
                    else:
                        table[i][j] = (s[i] == s[j]) and table[i + 1][j - 1]
            return table

        res = []
        table = buildTable(s)
        dfs(s, 0, [])
        return res
