
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0: return 0
        elif len(nums) == 1: return nums[0]
        # As the houses form a circle, if rob the 1st house,
        # you cannot rob the last one, so need 2 dp scan.
        return max(self.roblinear(nums[:len(nums ) -1]), self.roblinear(nums[1:]))

    def roblinear(self, nums):
        n = len(nums)
        if n == 1: return nums[0]
        dp = [nums[0]]
        dp.append(max(nums[1], dp[0]))
        for i in range(2, n):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i]))
        return dp[n - 1]

    def rob_dp(self, nums):  # O(n) time, O(1) space
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[:2])
        # The first iteration to find the maximum amount of money
        # after robbing the houses of 0 to n-1.
        pre, curr = nums[0], max(nums[:2])
        for i in xrange(2, n - 1):
            pre = max(pre + nums[i], curr)
            pre, curr = curr, pre
        maxval = curr
        # the second iteration to find the maximum amount of money
        # after robbing the houses of 1 to n.
        pre, curr = nums[1], max(nums[1:3])
        for i in xrange(3, n):
            pre = max(pre + nums[i], curr)
            pre, curr = curr, pre
        maxval = max(maxval, curr)
        return maxval
