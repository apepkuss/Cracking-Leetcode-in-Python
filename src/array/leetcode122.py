
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofits = 0
        n = len(prices)
        if n==0: return maxprofits
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                maxprofits += prices[i] - prices[i-1]
        return maxprofits
