

class Solution(object):
    """
    @ Linkedin, Bloomberg, Microsoft

    Array, DP, Divide and Conquer

    Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

    For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
    the contiguous subarray [4,-1,2,1] has the largest sum = 6.


    Kadane's algorithm:

    Initialize:
        max_so_far = minimum integer
        max_ending_here = 0

    Loop for each element in nums:
        max_ending_here += nums[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far

    """
    def maxSubArray_kadane(self, nums): # O(n) time
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = -2**32-1
        max_ending_here = 0

        for i in range(0, len(nums)):
            max_ending_here = max_ending_here + nums[i]

            if max_so_far < max_ending_here:
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0

        return max_so_far

    def maxSubArray_dp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = nums[0]
        max_so_far = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_so_far = max(max_so_far, curr_max)

        return max_so_far
