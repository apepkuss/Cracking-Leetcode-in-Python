

class Solution(object):
    def minimumTotal_dp1(self, triangle):  # Space: O(n^2)
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        dp = [[0]*m for _ in xrange(m)]
        dp[m-1] = triangle[m-1]
        for x in xrange(m-2, -1, -1):
            for y in xrange(x+1):
                dp[x][y] = min(dp[x+1][y], dp[x+1][y+1])+triangle[x][y]
        return dp[0][0]

    def minimumTotal_dp2(self, triangle):  # Space: O(n)
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)

        dp = [0] * m
        for i in range(m):
            dp[i] = triangle[m-1][i]

        # bottom-up way to computer the path sum level by level
        for x in xrange(m-2, -1, -1):
            for y in xrange(x+1):
                dp[y] = min(dp[y], dp[y+1]) + triangle[x][y]
        return dp[0]

    def minimumTotal_dp3(self, triangle):  # Space: O(1) in-place
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        for x in xrange(m-2, -1, -1):
            for y in xrange(x+1):
                triangle[x][y] += min(triangle[x+1][y], triangle[x+1][y+1])
        return triangle[0][0]
