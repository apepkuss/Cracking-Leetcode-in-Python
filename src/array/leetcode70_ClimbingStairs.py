

class Solution(object):
    """
    @ Adobe, Apple
    
    DP
    
    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    
    Note: Given n will be a positive integer.
    """
    def climbStairs_dp1(self, n):  # O(n) time, O(n) space
        assert n >= 0

        # dp[i] indicates the number of ways of climbing i stairs to the top
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2

        for x in range(3, n+1):
            dp[x] = dp[x-1]+dp[x-2]

        return dp[n]

    def climbStairs_dp2(self, n):  # O(n) time, O(1) space
        """
        :type n: int
        :rtype: int
        """
        assert n >= 0

        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        first, second, third = 1, 2, 0
        for i in range(3, n+1):
            third = first + second
            first, second = second, third

        return third


if __name__ == "__main__":
    res = Solution().climbStairs_dp1(6)
    print res
    res = Solution().climbStairs_dp2(6)
    print res
