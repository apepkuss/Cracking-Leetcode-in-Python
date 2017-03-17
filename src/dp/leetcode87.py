

class Solution(object):
    def isScramble_dp(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)!=len(s2): return False
        n = len(s1)
        # dp[i][j][k] means if s2[j,j+k-1] are scrambled by s1[i,i+k-1]
        dp = [[[False for k in xrange(n+1)] for j in xrange(n)] for i in xrange(n)]

        for k in xrange(1, n+1):
            for i in xrange(n+1-k):
                for j in xrange(n+1-k):
                    if k==1: dp[i][j][k] = s1[i]==s2[j]
                    else:
                        for l in xrange(1, k):
                            dp[i][j][k] = dp[i][j][l] and dp[i + l][j + l][k - l] or dp[i][j + k - l][l] and \
                                                                                     dp[i + l][j][k - l]
                            if dp[i][j][k]:
                                break
        return dp[0][0][n]

    def isScramble_recursive(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)!=len(s2): return False
        if s1==s2: return True

        # pruning
        l1 = list(s1)
        l2 = list(s2)
        l1.sort()
        l2.sort()
        if l1!=l2: return False

        n = len(s1)
        for i in range(1,n):
            if self.isScramble_recursive(s1[:i], s2[:i]) and self.isScramble_recursive(s1[i:], s2[i:]):
                return True
            if self.isScramble_recursive(s1[:i], s2[n-i:]) and self.isScramble_recursive(s1[i:], s2[:n-i]):
                return True
        return False


if __name__ == "__main__":
    s1 = "abcdefghijklmn"
    s2 = "efghijklmncadb"

    mysolution = Solution()
    res = mysolution.isScramble_recursive(s1, s2)
    print res