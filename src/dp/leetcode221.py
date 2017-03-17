

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in xrange(m)]
        dp[0][0] = matrix[0][0]
        width = 0
        for i in xrange(0, m):
            for j in xrange(0, n):
                if matrix[i][j]=='0':
                    dp[i][j] = 0
                elif i==0 or j==0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                width = max(width, dp[i][j])
        return width*width
