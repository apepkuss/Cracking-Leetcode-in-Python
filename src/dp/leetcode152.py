

class Solution(object):
    def maxProduct_fastDP(self, nums):  # O(n) time, O(n) space
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0: return n
        # current max product
        maxp = nums[0]
        # current min product
        minp = nums[0]
        # max product
        maxproduct = nums[0]
        for i in range(1, n):
            tmp = maxp
            maxp = max(maxp*nums[i], nums[i], minp*nums[i])
            minp = min(tmp*nums[i], nums[i], minp*nums[i])
            maxproduct = max(maxproduct, maxp)
        return maxproduct

    def maxProduct_slowDP(self, nums):  # MLE on OJ, O(n^2) time, O(n^2) space
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return n
        dp = [[0] * n for i in range(n)]
        maxproduct = -10000
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = dp[i][j - 1] * nums[j]
                maxproduct = max(maxproduct, dp[i][j])
        return maxproduct


