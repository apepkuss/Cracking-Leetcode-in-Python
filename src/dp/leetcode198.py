
class Solution(object):
    def rob_dp1(self, nums): # O(n) time, O(n) space
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n== 0: return 0
        dp = [0 for _ in xrange(n)]
        dp[0] = nums[0]
        for i in xrange(1, n):
            if i == 1:
                dp[i] = nums[i] if dp[i - 1] < nums[i] else dp[i - 1]
                continue
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

    def rob_dp2(self, nums):  # O(n) time, O(1) space
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        pre, curr = nums[0], max(nums[0:2])
        for i in xrange(2, n):
            pre = max(curr, pre + nums[i])
            pre, curr = curr, pre
        return curr
