
class Solution(object):
    """
    @ Microsoft, Google
    
    A peak element is an element that is greater than its neighbors.

    Given an input array where num[i] != num[i+1], find a peak element and return its index.

    The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

    For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
    """
    def findPeakElement_BS(self, nums):  # RT: O(logn)
        size = len(nums)
        return self.search(nums, 0, size - 1)

    def search(self, nums, start, end):
        if start == end:
            return start
        if start + 1 == end:
            if nums[start] < nums[end]:
                return end
            else:
                return start

        mid = (start + end) / 2
        if nums[mid] < nums[mid - 1]:
            return self.search(nums, start, mid - 1)
        if nums[mid] < nums[mid + 1]:
            return self.search(nums, mid + 1, end)
        return mid

    def findPeakElement_traverse(self, nums):  # RT: O(n)
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(1, n-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i
        if nums[0] < nums[n-1]:
            return n-1
        else:
            return 0
