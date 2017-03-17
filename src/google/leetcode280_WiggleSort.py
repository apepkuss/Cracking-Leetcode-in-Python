

class Solution(object):
    """
    @ Google

    Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

    For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
    """

    # Method 1: The idea is sorting the list of integers first, and then switching every neighbor two nodes from
    #           index 1 to last.
    # Notice: this question allows =, so we can use sorting in the simple solution.
    def wiggleSort_simple(self, nums): # O(nlogn) time
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        for i in range(1, n-1, 2):
            if i+1 < n:
                nums[i], nums[i+1] = nums[i+1], nums[i]

    # Method 2: The idea is based on the fact that if we make sure that all even positioned (at index 0, 2, 4, ..)
    #           elements are greater than their adjacent odd elements, we don't need to worry about odd positioned
    #           element.
    def wiggleSort_oneIteration(self, nums):  # O(n) time
        n = len(nums)
        for i in range(1, n, 2):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            if i + 1 < n and nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]