
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n== 0: return 0
        # the profits gained in the first i days
        profits1 = [0 for _ in range(n)]
        # the profits gained in the last i days
        profits2 = [0 for _ in range(n)]

        # compute the profits gained in the first transaction
        minprice = prices[0]
        for i in range(1, n):
            profits1[i] = max(profits1[i - 1], prices[i] - minprice)
            minprice = min(minprice, prices[i])

        # compute the profits gained in the second transaction
        maxprice = prices[n - 1]
        for i in range(n - 2, -1, -1):
            profits2[i] = max(profits2[i + 1], maxprice - prices[i])
            maxprice = max(maxprice, prices[i])

        # merge the profits gained in these two transactions
        return max([x+y for x, y in zip(profits1, profits2)])

if __name__ == "__main__":
    prices = [1,2]
    res = Solution().maxProfit(prices)
    print res
