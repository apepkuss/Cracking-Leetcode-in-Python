

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size < 2:
            return 0

        # the profits of the i-th day when have stocks in hand
        holdDP = [None] * size
        # the profits of the i-th day when have no stocks in hand
        notHoldDP = [None] * size

        notHoldDP[0], notHoldDP[1] = 0, max(0, prices[1] - prices[0])
        holdDP[0], holdDP[1] = -prices[0], max(-prices[0], -prices[1])
        for x in range(2, size):
            notHoldDP[x] = max(notHoldDP[x-1], holdDP[x - 1] + prices[x])
            holdDP[x] = max(holdDP[x-1], notHoldDP[x - 2] - prices[x])
        return notHoldDP[-1]
