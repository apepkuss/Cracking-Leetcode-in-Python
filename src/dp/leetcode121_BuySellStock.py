
class Solution(object):
    """
    @ Amazon, Microsoft, Bloomberg, Uber, Facebook

    Say you have an array for which the ith element is the price of a given stock on day i.

    If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
    design an algorithm to find the maximum profit.

    Example 1:
    Input: [7, 1, 5, 3, 6, 4]
    Output: 5

    max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
    Example 2:
    Input: [7, 6, 4, 3, 1]
    Output: 0

    In this case, no transaction is done, i.e. max profit = 0.
    """
    def maxProfit_dp1(self, prices): # O(n) time, O(n) space
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n== 0: return 0
        dp = [0 for _ in xrange(n)]
        minprice = prices[0]
        for x in xrange(1, n):
            if prices[x] > minprice:
                dp[x] = max(prices[x] - minprice, dp[x - 1])
            else:
                minprice = prices[x]
                dp[x] = dp[x - 1]
        return dp[n-1]

    def maxProfit_dp2(self, prices):  # O(n) time, O(1) space
        if prices is None or len(prices) == 0:
            return 0
        n = len(prices)
        min_price, curr_profit = prices[0], 0
        for i in xrange(1, n):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                curr_profit = max(curr_profit, prices[i] - min_price)
        return curr_profit

