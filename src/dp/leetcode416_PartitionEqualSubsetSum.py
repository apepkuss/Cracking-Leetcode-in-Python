
class Solution(object):
    """
    @ eBay

    dp

    Given a non-empty array containing only positive integers, find if the array can be partitioned into
    two subsets such that the sum of elements in both subsets is equal.

    Note:
        Each of the array element will not exceed 100.
        The array size will not exceed 200.
        Example 1:

        Input: [1, 5, 11, 5]

        Output: true

        Explanation: The array can be partitioned as [1, 5, 5] and [11].
        Example 2:

        Input: [1, 2, 3, 5]

        Output: false

        Explanation: The array cannot be partitioned into equal sum subsets.
    """

    # The idea to solve this problem has two main steps:
    # Step1. Check if the total sum of all elements in the array is even.
    #        If the sum is odd, the array cannot be paritioned into two
    #        subsets that have same sum. So, return False.
    # Step2. If the total sum is even, then find a subset of the array with
    #        sum equal to totalsum/2.




    def canPartition_recursive(self, nums): # O(2^n) time, as each element is considered twice (inclusive and exclusive).
        """
        :type nums: List[int]
        :rtype: bool
        """

        def dfs(nums, k, val):
            """
            Check if there is a subset with sum equal to val
            k: the number of elements to check. Current subset should be [0..k-1]
            Reduce this problem into two sub-problems:
            1. Do search val in [0..k-2]
            2. Do search val-nums[k-1] in [0..k-2]
            """
            if val == 0: return True
            if k == 0: return False

            if nums[ k -1] > val:
                return dfs(nums, k- 1, val)
            else:
                return dfs(nums, k - 1, val) or dfs(nums, k - 1, val - nums[k - 1])

        if nums is None: return False
        if len(nums) == 0: return True

        # if a set can be partitioned into two subsets with equal sum,
        # then the sum of all elements should be even.
        asum = sum(nums)
        if asum & 1 > 0:
            return False

        # check if there is a subset with sum equal to asum/2
        return dfs(nums, len(nums), asum / 2)

    def canPartition_dp(self, nums): # O(sum(nums) * len(nums)) time
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None: return False
        if len(nums) == 0: return True

        # if a set can be partitioned into two subsets with equal sum,
        # then the sum of all elements should be even.
        asum = sum(nums)
        if asum & 1 > 0: return False

        n = len(nums)
        # table[i][j] means if the sum of first j elements in nums is i,
        # where 0 <= i <= sum(nums)/2, 0 <= j <= len(nums)
        table = [[False for j in range(n + 1)] for i in range(asum + 1)]

        # initialize table
        # The first column is set False
        for i in range(1, asum / 2 + 1):
            table[i][0] = False

        # The first row is set True
        for j in range(n + 1):
            table[0][j] = True

        for i in range(1, asum / 2 + 1):
            for j in range(1, n + 1):
                if i < nums[j - 1]:
                    table[i][j] = table[i][j - 1]
                else:
                    table[i][j] = table[i][j - 1] or table[i - nums[j - 1]][j - 1]

        return table[asum / 2][n]










