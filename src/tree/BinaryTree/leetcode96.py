
class Solution(object):
    """
    @ Snapchat

    Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

    For example,
    Given n = 3, there are a total of 5 unique BST's.
    """
    def numTrees_recursive(self, n): # LTE error
        # base case
        if n== 0 or n == 1:
            return 1
        # recursive step
        res = 0
        for i in xrange(n):
            res += self.numTrees_recursive(i) * self.numTrees_recursive(n - 1 - i)
        return res

    def numTrees_dp(self, n):  # RT: O(n^2), Space: O(n) for DP
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1]
        if n <= 1: return dp[n]
        for i in range(2, n + 1):
            value = 0
            for j in range(i):
                value += dp[j] * dp[i - 1 - j]
            dp.append(value)
        return dp[-1]