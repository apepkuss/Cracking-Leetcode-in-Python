class Solution(object):
    def search(self, nums, target): # RT: O(log(n)), space: O(1)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end)/2
            if nums[mid] == target: return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid+1
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid+1
                else:
                    end = mid
        return -1