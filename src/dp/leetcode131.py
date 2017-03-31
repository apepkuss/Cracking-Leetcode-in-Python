

class Solution(object):
    """
    @ Bloomberg

    Backtracing

    Given a string s, partition s such that every substring of the partition is a palindrome.

    Return all possible palindrome partitioning of s.

    For example, given s = "aab",
    Return

    [
      ["aa","b"],
      ["a","a","b"]
    ]
    """

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        if len(s) > 0:
            table = self.build_table(s)
            self.dfs(s, 0, [], res, table)
        return res

    def build_table(self, s):  # O(n^2) in time and space
        """
        build up a look-up table, which is used in dfs function
        :param s:
        :return:
        """
        n = len(s)
        # table[i][j] denotes if substring s[i...j] is palindromic or not
        table = [[False] * n for _ in range(n)]

        for l in range(1, n+1):
            for i in range(n-l+1):
                j = (i + l - 1) % n
                if i == j:
                    table[i][j] = True
                elif i == j-1:
                    table[i][j] = s[i] == s[j]
                else:
                    table[i][j] = s[i] == s[j] and table[i + 1][j - 1]

        return table

    def dfs(self, s, start, valuelist, res, table):
        if len(s) == start:
            res.append(valuelist)
            return

        for l in range(1, len(s[start:]) + 1):
            if table[start][start + l - 1]:
                self.dfs(s, start + l, valuelist + [s[start:start + l]], res, table)


if __name__ == "__main__":
    s = "efe"
    res = Solution().partition(s)
    print res





