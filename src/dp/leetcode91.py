

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="" or s[0]=='0': return 0
        dp = [1,1]
        for i in range(2, len(s)+1):
            if s[i-1]!='0' and (10<int(s[i-2:i])<20 or 21<=int(s[i-2:i])<=26):
                dp.append(dp[i-2]+dp[i-1])
            elif int(s[i-2:i])==10 or int(s[i-2:i])==20:
                dp.append(dp[i-2])
            elif s[i-1]!='0':
                dp.append(dp[i-1])
            else:
                return 0

        return dp[len(s)]
