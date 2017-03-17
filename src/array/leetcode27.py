
class Solution(object):
    def removeElement_start_start(self, nums, val):  # O(n) time
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0: return 0
        i = j = 0
        while i<len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j+=1
            i+=1
        return j

    def removeElement_start_end(self, nums, val):  # O(n) time
        if len(nums) == 0: return 0
        i, j = 0, len(nums)-1
        while i<j:
            if nums[i]!=val: i += 1
            else:
                while i<j and nums[j] == val:
                    j -= 1
                if i==j: return i
                else:
                    nums[i] = nums[j]
                    j -= 1
                while i<j and nums[j]==val:
                    j -= 1
        if nums[i]==val: return i
        else: return i+1
