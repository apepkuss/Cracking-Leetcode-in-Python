import math, sys

class Solution(object):
    """
    @ Google

    DP, Math

    Given a positive integer n, find the least number of perfect square numbers
    (for example, 1, 4, 9, 16, ...) which sum to n.

    For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
    return 2 because 13 = 4 + 9.
    """

    def numSquares_four(self, n):
        """
        Lagrange's four_square theorem
        :param n:
        :return:
        """
        if n== 0: return 0
        while n % 4 == 0: n /= 4
        if n % 8 == 7: return 4
        m = int(n ** 0.5) + 1
        for x in xrange(m):
            y = int((n - x * x) ** 0.5)
            if x * x + y * y == n:
                if x > 0 and y > 0:
                    return 2
                else:
                    return 1
        return 3

    def numSquares_dp(self,n ):
        # table[i] means the least number of perfect square numbers for integer i
        table = [0, 1]
        if n == 0 or n == 1:
            return table[n]
        i = 2
        while i <= n:
            k = int(i**0.5)
            minval = i
            for j in range(1, k+1):
                minval = min(minval, table[i - j**2])
            table.append(minval+1)
            i += 1
        return table[n]


if __name__ == "__main__":
    mysolution = Solution()
    res = mysolution.numSquares_dp(15)
    print res
