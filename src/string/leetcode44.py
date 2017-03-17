

class Solution(object):
    """
    @ Google, Snapchat, Facebook

    Implement wildcard pattern matching with support for '?' and '*'.
    """

    def isMatch_recursive(self, s, p): # TLE error
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def dfs(s, p):
            if len(s) == 0 and len(p) == 0:
                return True
            elif len(p) == 0:
                return False
            elif len(s) == 0:
                return len(p) == p.count('*')
            elif s == p:
                return True
            elif s[0] == p[0] or p[0] == '?':
                return dfs(s[1:], p[1:])
            elif p[0] == '*':
                i = 0
                while i < len(s) + 1 and not dfs(s[i:], p[1:]):
                    i += 1
                return i <= len(s)
            return False

        if len(p) - p.count('*') > len(s):
            return False
        pattern = []
        first = True
        for i in xrange(len(p)):
            if p[i] == '*':
                if first:
                    pattern.append(p[i])
                    first = False
            else:
                pattern.append(p[i])
                first = True
        p = ''.join(pattern)
        return dfs(s, p)

    def isMatch_dp(self, s, p): # RT: O(n^2), Space: O(n^2)
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) - p.count('*') > len(s): return False

        # replace multiple * with one *
        # e.g., a***b**c => a*b*c
        pattern = []
        isFirst = True
        for i in range(len(p)):
            if p[i]=='*':
                if isFirst:
                    pattern.append(p[i])
                    isFirst = False
            else:
                pattern.append(p[i])
                isFirst = True
        m, n = len(s), len(pattern)

        # dp[i][j] indicates s[:i] and pattern[:j] is matched or not.
        dp=[[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0]=True
        if n>0 and pattern[0]=='*': dp[0][1] = True

        # populate the dp matrix
        for i in range(1, m+1): # for string
            for j in range(1, n+1): # for pattern
                if pattern[j-1]=='*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif s[i-1]==pattern[j-1] or pattern[j-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
        return dp[m][n]

    def isMatch_iterative(self, s, p): # RT: O(n), Space: O(1)
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # the position of the last occurrence of * in p
        lastStartPos = -1
        # the position of the last character in s which
        # matches with *
        lastCharMatchStar = 0
        idxPattern = idxStr = 0
        while idxStr < len(s):
            # when there is a match, continue to compare
            # the characters in s and p
            if idxPattern<len(p) and (s[idxStr]==p[idxPattern] or p[idxPattern]=='?'):
                idxStr += 1
                idxPattern += 1
            # when * comes, save the positions of idxPattern
            # and idxStr
            elif idxPattern<len(p) and p[idxPattern]=='*':
                lastStartPos = idxPattern
                lastCharMatchStar = idxStr
                idxPattern+=1
            # when there is a conflict, and we have a star,
            # reset idxPattern to point to the next position
            # of previous, and also move lastCharMatchStar
            # to its next position, and set idxStr to point
            # to lastCharMatchStar's position;
            # after these settings, continue to check
            elif lastStartPos!=-1:
                idxPattern = lastStartPos+1
                lastCharMatchStar += 1
                idxStr = lastCharMatchStar
            # if all the conditions are not satisfied,
            # s does not match p.
            else: return False
        while idxPattern<len(p) and p[idxPattern]=='*':
            idxPattern += 1
        if idxPattern == len(p): return True
        return False



if __name__ == "__main__":
    s = 'aa'
    p = '*'
    res = Solution().isMatch_iterative(s, p)
    print res
