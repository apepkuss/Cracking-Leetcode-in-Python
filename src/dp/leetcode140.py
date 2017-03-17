
class Solution(object):
    def wordBreak_dp1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """

        def dfs(s, stringlist):
            if check(s):
                if len(s) == 0:
                    res.append(stringlist[1:])
                    return
                for i in xrange(1, len(s) + 1):
                    if s[:i] in wordDict:
                        dfs(s[i:], stringlist + ' ' + s[:i])

        # check if s can be partitioned based on dict
        def check(s):
            n = len(s)
            dp = [False for _ in xrange(n + 1)]
            dp[0] = True
            for l in xrange(1, n + 1):
                for i in xrange(l):
                    if dp[i] and s[i:l] in wordDict:
                        dp[l] = True
                        break
            return dp[n]

        # to find partition ways, need to use dfs based
        # on dp result
        res = []
        dfs(s, '')
        return res

    def wordBreak_dp2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def dfs(start, valuelist):
            """
            Depth-first traverse the decision tree by backtracking algorithm
            :param wordlist: the dictionary of words
            """
            # base case
            if start == len(s):
                res.append(valuelist[1:])
                return

            # recursive step by backtracking
            for l in xrange(self.minlen, 1 + min(len(s) - start, self.maxlen)):
                if s[start:start + l] in wordDict and (start + l == len(s) or table[start + l][len(s) - 1]):
                    dfs(start + l, valuelist + ' ' + s[start:start + l])

        def buildTable(s):
            """
            check if s can be partitioned based on dict
            """
            n = len(s)
            # table[i][j] denotes if s[i...j] can be segmented into the words in wordDict
            table = [[False for j in xrange(n)] for i in xrange(n)]
            for l in xrange(self.minlen, n + 1):
                for i in xrange(n - l + 1):
                    j = i + l - 1
                    if s[i:j + 1] in wordDict:
                        table[i][j] = True
                    else:
                        for k in xrange(i + self.minlen, j - self.minlen + 2):
                            if table[i][k - 1] and table[k][j]:
                                table[i][j] = True
                                break
            return table

        self.maxlen = 0
        self.minlen = 10000
        for word in wordDict:
            self.maxlen = max(self.maxlen, len(word))
            self.minlen = min(self.minlen, len(word))

        table = buildTable(s)
        res = []
        dfs(0, '')
        return res

if __name__ == "__main__":
    mysolution = Solution()
    res = mysolution.wordBreak_dp2("catsanddog", ["cat","cats","and","sand","dog"])
    print res