class Solution(object):
    """
    @ Google
    
    Backtracking, DP
    
    Given a non-negative integer n, count all numbers with unique digits, x, where 0 <= x < 10n.

    Example:
    Given n = 2, return 91. (The answer should be the total numbers in the range of 0 <= x < 100, 
    excluding [11,22,33,44,55,66,77,88,99])
    """

    # Method 1: backtracking
    def countNumbersWithUniqueDigits_backtrack(self, n):  # MLE error
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        if n == 1: return 10

        # if n > 1
        res = ['0']
        for c in '123456789':
            self.backtrack(n - 1, '' + c, res)
        return len(res)

    def backtrack(self, n, values, res):
        res.append(values)
        if n > 0:
            for c in '0123456789':
                if c not in values:
                    self.backtrack(n - 1, values + c, res)


    # Method 2: dynamic programming
    def countNumbersWithUniqueDigits_dp(self, n):  # O(n^2) in time, O(n) in space
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        if n == 1: return 10

        # dp[i] denotes the numbers with [0..i] unique digits
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 10

        for i in range(2, n + 1):
            # compute the numbers with i unique digits
            curr = 9
            for k in range(2, i + 1):
                curr *= 9 - (k - 2)
            dp[i] = dp[i - 1] + curr

        return dp[n]



