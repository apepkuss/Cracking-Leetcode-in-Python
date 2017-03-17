

class Solution(object):
    def maxCoins(self, nums): # O(n) time, O(n) space
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1: return nums[0]
        nums = [1] + nums + [1]
        n = len(nums)
        # table[i][j] denotes the maximum coins between i and j, exclusive.
        table = [[0] * n for _ in xrange(n)]
        for l in xrange(2, n):
            for i in xrange(n - l):
                j = i + l
                for k in xrange(i + 1, j):
                    table[i][j] = max(table[i][j], table[i][k] + nums[i] * nums[k] * nums[j] + table[k][j])
        return table[0][n - 1]
