

class Solution(object):
    def minPathSum_dfs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(row, col, asum):
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                self.minsum = min(self.minsum, asum)
                return
            if row < len(grid) - 1:
                dfs(row + 1, col, asum + grid[row + 1][col])
            if col < len(grid[0]) - 1:
                dfs(row, col + 1, asum + grid[row][col + 1])

        if grid is None or len(grid) == 0:
            return 0
        import sys
        self.minsum = sys.maxint
        dfs(0, 0, grid[0][0])
        return self.minsum

    def minPathSum_dp1(self, grid): # O(n^2) time, O(n^2) space
        m = len(grid);
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]

    def minPathSum_dp2(self, grid): # O(n^2) time, O(n) space
        if grid is None or len(grid) == 0: return 0
        m, n = len(grid), len(grid[0])
        table = [0 for _ in xrange(n)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0:
                    if j == 0:
                        table[j] = grid[i][j]
                    else:
                        table[j] = table[j-1] + grid[i][j]
                else:
                    if j == 0:
                        table[j] += grid[i][j]
                    else:
                        table[j] = grid[i][j] + min(table[j - 1], table[j])
        return table[n - 1]


if __name__ == "__main__":
    grid = [[1,2],[1,1]]
    res = Solution().minPathSum_dp2(grid)
    print res
