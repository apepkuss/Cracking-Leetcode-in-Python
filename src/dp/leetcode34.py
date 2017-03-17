
def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid); n = len(grid[0])
    # dp[i][j]: the minimum sum from (0,0) to (i,j)
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # initialize the dp table
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[0][i] = dp[0][ i -1] + grid[0][i]
    for i in range(1, m):
        dp[i][0] = dp[ i -1][0] + grid[i][0]

    # populate the dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]

