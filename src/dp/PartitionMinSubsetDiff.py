

class Solution(object):
    """
    @ Google

    dp

    Given a set of integers, the task is to divide it into two sets S1 and S2 such that the
    absolute difference between their sums is minimum.

    If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must
    have n-m elements and the value of abs(sum(Subset1) - sum(Subset2)) should be minimum.

    Example:

    Input:  arr[] = {1, 6, 11, 5}
    Output: 1
    Explanation:
    Subset1 = {1, 5, 6}, sum of Subset1 = 12
    Subset2 = {11}, sum of Subset2 = 11

    Reference: http://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
    """

    def findMin_recursive(self, nums): # O(2^n) time

        def dfs(nums, k, currsum, totalsum):
            if k == 0:
                return abs((totalsum - currsum) - currsum)
            return min(dfs(nums, k-1, currsum, totalsum), dfs(nums, k-1, currsum+nums[k-1], totalsum))

        n = len(nums)
        if n==0: return 0

        total = sum(nums)
        return dfs(nums, n, 0, total)

    def findMin_dp(self, nums):

        n = len(nums)
        if n==0: return 0

        m = sum(nums)

        # table[i][j] means the sum of first j elements of nums is i,
        # where 0 <= i <= m, 0 <= j <= n
        table = [[False for j in range(n+1)] for i in range(m+1)]

        # initialize first column, except table[0][0], as False
        for i in range(1, m+1):
            table[i][0] = False
        # initialize first row as True. O sum is possible with all elements
        for j in range(n+1):
            table[0][j] = True

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i < nums[j]:
                    table[i][j] = table[i][j-1]
                else:
                    table[i][j] = table[i][j] or table[i-nums[j-1]][j-1]

        diff = 0
        for i in range(m/2, -1, -1):
            if table[i][n]:
                diff = sum - 2*j
                break
        return diff


