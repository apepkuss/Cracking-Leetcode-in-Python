
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(depth, start, valuelist):
            if valuelist not in res:
                res.append(valuelist)

            if depth==len(nums):
                return

            for i in range(start, len(nums)):
                if i==start or (i>start and nums[i]!=nums[i-1]):
                    dfs(depth+1, i+1, valuelist + [nums[i]])
        res = []
        nums.sort()
        dfs(0, 0, [])
        return res
