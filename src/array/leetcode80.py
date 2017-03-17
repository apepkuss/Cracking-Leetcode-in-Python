
class Solution(object):
    # A generic implementation for "at most k duplicates" problems
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2: return len(nums)

        # k indicates the duplicates allowed.
        k = 2
        i = k
        for j in range(k, len(nums)):
            if nums[j] != nums[i-k]:
                nums[i] = nums[j]
                i += 1
        return i