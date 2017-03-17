
class Solution(object):
    def canJump_linear1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        step = nums[0]
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else:
                return False
        return True

    def canJump_linear2(self, nums):
        n = len(nums)
        if n == 0 or n == 1: return True
        rightmost = 0
        for i in xrange(n):
            if i == 0:
                rightmost = nums[0]
            else:
                rightmost = max(rightmost, nums[i] + i)
            if rightmost == i and i < n - 1 and nums[i] == 0:
                return False
            elif rightmost >= n - 1:
                return True
