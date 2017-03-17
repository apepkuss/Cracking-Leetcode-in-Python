

class Solution(object):
    """
    @ Snapchat, Uber

    Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the
    candidate numbers sums to T.

    The same repeated number may be chosen from C unlimited number of times.

    Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.
    For example, given candidate set [2, 3, 6, 7] and target 7,
    A solution set is:
    [
      [7],
      [2, 2, 3]
    ]
    """
    def combinationSum1(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(t, start, valuelist):
            # base case
            if t==0:
                return res.append(valuelist)

            # recursive step
            for i in xrange(start, len(candidates)):
                if candidates[i]<=t:
                    dfs(t-candidates[i], i, valuelist+[candidates[i]])
        # sorting for monotony of the resulted sequence and optimizing the candidate pool
        candidates.sort()
        res = []
        dfs(target, 0, [])
        return res

    def combinationSum(self, candidates, target):
        def dfs(start, asum, valuelist):
            if asum == target:
                res.append(valuelist)
                return

            for i in xrange(start, len(candidates)):
                if asum + candidates[i] > target:
                    return
                dfs(i, asum + candidates[i], valuelist + [candidates[i]])

        candidates.sort()
        res = []
        dfs(0, 0, [])
        return res


if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    res = Solution().combinationSum(candidates, target)
    print res
