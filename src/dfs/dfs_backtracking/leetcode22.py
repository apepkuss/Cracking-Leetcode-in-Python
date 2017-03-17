

class Solution(object):
    def generateParenthesis1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(left, right, valuelist):
            if left<0 or right<0:
                return
            if left==right==0:
                res.append(valuelist)
            elif left==right:
                dfs(left-1, right, valuelist+'(')
            elif left<right:
                dfs(left-1, right, valuelist+'(')
                dfs(left, right-1, valuelist+')')

        res = []
        dfs(n,n,'')
        return res

    def generateParenthesis(self, n):
        def dfs(left, rite, valuelist):
            if left < 0 or rite < 0:
                return
            if left == rite == 0:
                res.append(valuelist)
                return

            if left == rite:
                dfs(left - 1, rite, valuelist + '(')
            elif left < rite:
                dfs(left - 1, rite, valuelist + '(')
                dfs(left, rite - 1, valuelist + ')')

        res = []
        dfs(n, n, '')
        return res

if __name__ == "__main__":
    res = Solution().generateParenthesis(3)
    print res