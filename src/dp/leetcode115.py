
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s ) +1, len(t ) +1
        # dp[i][j] denotes the number of substring t[0:j] in substring s[0:i]
        dp = [[0 for j in xrange(n)] for i in xrange(m)]

        # initialize the dp table
        for i in xrange(m):
            dp[i][0] = 1

        # populate the dp table
        for i in range(1, m):
            for j in range(1, min( i +1, n)):
                if s[ i -1] == t[ j -1]:
                    dp[i][j] = dp[ i -1][j] + dp[ i -1][ j -1]
                else:
                    dp[i][j] = dp[ i -1][j]

        return dp[len(s)][len(t)]
