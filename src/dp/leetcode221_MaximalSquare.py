

class Solution(object):
    """
    @ Apple, Airbnb, Facebook
    
    DP
    
    Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

    For example, given the following matrix:
    
    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0
    Return 4.
    """
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])

        # dp[i][j] denotes the width of the maximal square between matrix(0,0) and matrix(i,j)
        dp = [[0]*n for _ in xrange(m)]

        # the width of the maximal square
        width = 0
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                elif i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

                width = max(width, dp[i][j])

        return width*width
