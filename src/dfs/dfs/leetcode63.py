
class Solution(object):

    def uniquePathsWithObstacles_dp1(self, obstacleGrid):  # O(n^2) time, O(n^2) space
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 ] *n for _ in xrange(m)]
        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        for x in xrange(m):
            for y in xrange(n):
                if x+1 < m and obstacleGrid[x+1][y] != 1:
                    dp[x+1][y] += dp[x][y]
                if y+1 < n and obstacleGrid[x][y+1] != 1:
                    dp[x][y+1] += dp[x][y]
        return dp[m - 1][n - 1]

    def uniquePathsWithObstacles_DFS(self, obstacleGrid):  # TLE error
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        self.cache = [[0] * (n + 1) for _ in xrange(m + 1)]
        if obstacleGrid[0][0]: return 0
        if m == 1 and n == 1: return 1
        return self.dfs(m, n, obstacleGrid)

    def dfs(self, m, n, obstacleGrid):
        if m < 1 or n < 1: return 0
        if obstacleGrid[m - 1][n - 1] == 1: return 0
        if m == 1 and n == 1: return 1
        if self.cache[m][n] > 0:
            return self.cache[m][n]
        else:
            self.cache[m][n] = self.dfs(m-1, n, obstacleGrid) + self.dfs(m, n-1, obstacleGrid)
            return self.cache[m][n]


if __name__ == "__main__":
    mysolution = Solution()
    res = mysolution.uniquePathsWithObstacles_dp1([[0],[0]])
    print res
