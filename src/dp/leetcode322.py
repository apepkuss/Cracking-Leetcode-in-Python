
class Solution(object):

    def coinChange_dp1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if coins is None or len(coins) == 0:
            return 0
        if amount == 0: return 0
        coins.sort()
        if amount < coins[0]: return -1
        # dp[i] denotes the minimum number of coins consisting of amount of i
        table = [0] + [-1] * amount
        candidates = []
        for c in coins:
            if c <= amount:
                table[c] = 1
                candidates.append(c)
        for i in xrange(candidates[0] + 1, amount + 1):
            if i not in coins:
                minvalue = -1
                for coin in candidates:
                    if i >= coin and table[i - coin] != -1:
                        if minvalue == -1:
                            minvalue = table[i - coin]
                        else:
                            minvalue = min(minvalue, table[i - coin])
                if minvalue > 0:
                    table[i] = 1 + minvalue
                else:
                    table[i] = minvalue
        return table[amount]

    def coinChange_dp2(self, coins, amount):
        if coins is None or len(coins) == 0:
            return 0
        if amount == 0: return 0
        # dp[i] denotes the minimum number of coins consisting of amount of i
        table = [0] + [-1] * amount
        for i in xrange(amount):
            if table[i] == -1:
                continue
            for c in coins:
                if i + c > amount:
                    continue
                if table[i + c] < 0 or table[i + c] > table[i] + 1:
                    table[i + c] = table[i] + 1
        return table[amount]

    def coinChange_dfs(self, coins, amount): # TLE

        def dfs(amount, valuelist):
            if amount == 0:
                return len(valuelist)
            for i in xrange(len(coins)):
                if coins[i] <= amount:
                    val = dfs(amount - coins[i], valuelist + [coins[i]])
                    if val != -1:
                        return val
            return -1

        if coins is None or len(coins) == 0:
            return 0
        coins.sort(reverse=True)
        return dfs(amount, [])


if __name__ == "__main__":
    coins = [186,419,83,408]
    amount = 6249
    res = Solution().coinChange_dfs(coins, amount)
    print res
