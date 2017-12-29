
class Solution(object):
    """
    @ Bloomberg

    Given an array S of n integers, find three integers in S such that the sum is
    closest to a given number, target. Return the sum of the three integers. You
    may assume that each input would have exactly one solution.
    For example, given array S = {-1, 2, 1, -4}, and target = 1. The sum that is
    closest to the target is 2. (-1 + 2 + 1 = 2).
    """
    def threeSumClosest(self, nums, target): # O(n^2) time
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # sort target array
        nums.sort()
        min_gap = 2 ** 32 - 1
        n = len(nums)
        for i in range(n-2):  # O(n^2)
            j = i + 1
            k = n - 1
            while j < k:
                asum = nums[i]+nums[j]+nums[k]
                min_gap = min(min_gap, abs(target - asum))
                if min_gap == 0:
                    return min_gap
                elif asum < target:
                    j += 1
                else:
                    k -= 1
        return min_gap
