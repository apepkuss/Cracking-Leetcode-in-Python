
class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n == 1: return 0
        jumpNum = 0
        currCanReach = 0
        lastCanReach = 0
        for x in xrange(n):
            if x > lastCanReach:
                lastCanReach = currCanReach
                jumpNum += 1
            currCanReach = max(currCanReach, x + nums[x])
        return jumpNum

