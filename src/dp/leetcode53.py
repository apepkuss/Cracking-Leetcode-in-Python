

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        thisSum = 0
        maxSum = -10000
        for i in range(0, len(nums)):
            if thisSum < 0:
                thisSum = 0
            thisSum = thisSum + nums[i]
            maxSum = max(thisSum, maxSum)
        return maxSum
