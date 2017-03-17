
class Solution(object):
    def nextPermutation(self, nums):    # O(n)
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        # From right to left, find the first digit (PartitionNumber) which violate the increase trend
        while i > 0:
            if nums[i] > nums[i-1]:
                break
            i -= 1
        if i == 0:
            nums.reverse()
        else:
            # From right to left, find the first digit (ChangeNumber), which is larger than PartitionNumber;
            # then, swap ChangeNumber and PartitionNumber
            for k in xrange(len(nums)-1, i-1, -1):
                if nums[i-1] < nums[k]:
                    nums[i-1], nums[k] = nums[k], nums[i-1]
                    break

            # Reverse all digits on the right side of partition index
            nums[i:] = nums[i:][::-1]
