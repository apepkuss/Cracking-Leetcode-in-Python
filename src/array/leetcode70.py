
class Solution(object):
    def climbStairs_dp1(self, n):  # O(n) time, O(n) space
        dp = [0 for _ in xrange(n+1)]
        dp[0] = 1
        dp[1] = 1
        for x in xrange(2, n+1):
            dp[x] = dp[x-1]+dp[x-2]
        return dp[n]

    def climbStairs_dp2(self, n):  # O(n) time, O(1) space
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 1
        if n==2: return 2

        a,b,c = 1,2,0
        for i in range(2, n):
            c = a + b
            a, b = b, c
        return c
