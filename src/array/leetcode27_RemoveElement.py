
class Solution(object):
    def removeElement_start_start(self, nums, val):  # O(n) time
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        assert nums is not None

        if len(nums) == 0:
            return 0

        i = j = 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1

        return j

    def removeElement_start_end(self, nums, val):  # O(n) time
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        assert nums is not None

        if len(nums) == 0:
            return 0

        i, j = 0, len(nums)-1
        while i <= j:
            while i <= j and nums[i] != val:
                i += 1

            while i <= j and nums[j] == val:
                j -= 1

            if i > j:
                break

            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return j + 1
