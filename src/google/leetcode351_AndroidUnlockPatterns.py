
class Solution(object):
    """
    @ Google

    Given an Android 3x3 key lock screen and two integers m and n, where 1 <= m <= n <= 9, count the total number of
    unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

    Rules for a valid pattern:
    Each pattern must connect at least m keys and at most n keys.
    All the keys must be distinct.
    If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have
    previously selected in the pattern. No jumps through non selected key is allowed.
    The order of keys used matters.
    """
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def dfs(curr, remain):
            if remain < 0:
                return 0
            if remain == 0:
                return 1
            visited[curr] = True
            res = 0
            for i in range(1, 10):
                if not visited[i] and (skip[curr][i] == 0 or visited[skip[curr][i]]):
                    res += dfs(i, remain- 1)
            visited[curr] = False
            return res

        # skip[i][j] == 0 means i and j are neighbors
        # skip[i][j] == k means k is between i and j
        skip = [[0] * 10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = skip[2][8] = skip[8][2] = 5
        visited = [False] * 10
        res = 0
        for i in range(m, n + 1):
            res += dfs(1, i - 1) * 4  # starts from 1, 3, 7, 9
            res += dfs(2, i - 1) * 4  # starts from 2, 4, 6, 8
            res += dfs(5, i - 1)      # starts from 5
        return res