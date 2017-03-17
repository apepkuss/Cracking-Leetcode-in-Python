
class Solution(object):
    def uniquePaths_dfs(self, m, n): # TLE error
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # base case
        if m< 1 or n < 1:
            return 0
        if m == 1 or n == 1:
            return 1
        # recursive step
        return self.uniquePaths_dfs(m-1, n) + self.uniquePaths_dfs(m, n-1)

    def uniquePaths_dp1(self, m, n):  # O(n^2) time, O(n^2) space
        # dp[i][j] denotes the number of unique paths from (0,0) to (i,j)
        dp = [[0] * n for _ in xrange(m)]
        dp[0][0] = 1
        # populate dp table
        for x in xrange(m):
            for y in xrange(n):
                if x + 1 < m:
                    dp[x+1][y] += dp[x][y]
                if y + 1 < n:
                    dp[x][y+1] += dp[x][y]

        return dp[m-1][n-1]

    def uniquePaths_dp2(self, m, n):  # O(n^2) time, O(n) space
        if m < n:
            m, n = n, m
        # dp[i] denotes the number of unique paths from (0,0) to (i,j)
        dp = [0 for _ in xrange(n)]
        dp[0] = 1
        # populate dp array
        for x in xrange(m):
            for y in xrange(n-1):
                dp[y+1] += dp[y]
        return dp[n-1]
