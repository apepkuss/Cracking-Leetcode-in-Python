class Solution(object):
    """
    @ Linkedin, Uber

    Numbers can be regarded as product of its factors. For example,

    8 = 2 x 2 x 2;
      = 2 x 4.
    Write a function that takes an integer n and return all possible combinations of its factors.

    Note:
    You may assume that n is always positive.
    Factors should be greater than 1 and less than n.
    """

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                m = n / i
                res.append([i, m])
                for q in self.getFactors(m):
                    if q[0] >= i:
                        res.append([i] + q)
        return res

    def getFactors_2(self, n): # MLE
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(start, n, valuelist):
            if n == 1:
                if len(valuelist) > 1:
                    res.append(valuelist)
                return
            for i in range(start, n+1):
                if n >= i:
                    if n % i == 0:
                        dfs(i, n / i, valuelist + [i])
                else:
                    break
            return

        res = []
        if n < 2: return res
        dfs(2, n, [])
        return res


if __name__ == "__main__":
    n = 12
    res = Solution().getFactors(n)
    print res
