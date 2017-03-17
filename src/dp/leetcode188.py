

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k > n / 2:
            return self.quickSolve(n, prices)
        # dp[i] denotes the profits after the i-th transaction
        dp = [None] * (2 * k + 1)
        dp[0] = 0
        for i in xrange(n):
            for j in xrange(1, 1+min(2 * k, i+1)):
                dp[j] = max(dp[j], dp[j-1] + prices[i] * [1, -1][j % 2])
        return dp[2 * k]

    def quickSolve(self, n, prices):
        sum = 0
        for x in xrange(n-1):
            if prices[x+1] > prices[x]:
                sum += prices[x+1] - prices[x]
        return sum
