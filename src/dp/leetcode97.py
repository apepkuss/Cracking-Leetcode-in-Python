

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2)!=len(s3):
            return False
        # dp[i][j] denotes if s3[0, i+j-1] consists of s1[0,i-1] and s2[0,j-1]
        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        dp[0][0] = True
        # initialize the first column
        for i in range(1, len(s1)+1):
            dp[i][0] = dp[i-1][0] and s3[i-1]==s1[i-1]
        # initialize the first row
        for j in range(1, len(s2)+1):
            dp[0][j] = dp[0][j-1] and s3[j-1]==s2[j-1]
        # populate other cells of the dp table
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        return dp[len(s1)][len(s2)]
