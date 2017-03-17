
class Solution(object):
    def removeDuplicates(self, nums):   # RT: O(n)
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        slow = 0
        for fast in xrange(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
