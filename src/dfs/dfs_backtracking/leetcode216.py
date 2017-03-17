
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(nums, start, k, n, valuelist):
            if n==0 and k==0: res.append(valuelist)
            if k==0: return
            for x in xrange(start, len(nums)):
                if n < nums[x]: return
                dfs(nums, x+1, k-1, n-nums[x], valuelist+[nums[x]])

        res = []
        nums = [i for i in xrange(1,10)]
        dfs(nums, 0, k, n, [])
        return res
