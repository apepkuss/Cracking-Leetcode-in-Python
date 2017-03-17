

class Solution(object):
    def minCut_dp(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i] indicates the minimum number of palindrome partitions in s[i:]
        dp = [0 for i in range(len(s) + 1)]
        # p[i][j] is True, if s[i,j] is palindromic; False, otherwise.
        p = [[False for i in range(len(s))] for j in range(len(s))]
        # set dp[i] the upper bound
        for i in range(len(s) + 1):
            dp[i] = len(s) - i
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                # case1: i==j
                # case2: i==j+1, and s[i]==s[j]
                # case3: s[i]==s[j], and s[i+1...j-1] is palindromic
                if i == j or (s[i] == s[j] and i + 1 == j) or (s[i] == s[j] and p[i + 1][j - 1]):
                    p[i][j] = True
                    dp[i] = min(1 + dp[j + 1], dp[i])
        return dp[0] - 1


if __name__ == "__main__":
    mysolution = Solution()
    s = "abcbb"
    res = mysolution.minCut_dp(s)
    print res